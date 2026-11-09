// Central de Ajuda Communicare — Worker de respostas com IA (Cloudflare Workers).
//
// Variáveis no painel do Cloudflare (Workers > Settings > Variables):
//   ANTHROPIC_API_KEY  (Secret)  chave da API do Claude
//   ALLOWED_ORIGIN     ex.: https://ajuda.communicare.com.br
//   KB_URL             ex.: https://ajuda.communicare.com.br/base.json
//   MODEL              opcional; padrão claude-haiku-5-5
//
// O Worker guarda a chave, busca os tutoriais no próprio site e só responde
// perguntas de quem está na Central de Ajuda. Limite de uso por IP: configurar
// uma regra de Rate Limiting no Cloudflare para a rota deste Worker.

const PROMPT_IA = "Você é o assistente da Central de Ajuda da Communicare, um sistema de gestão para clínicas e consultórios.\nResponda em português do Brasil, de forma direta e cordial, usando SOMENTE os tutoriais fornecidos entre <tutoriais>.\n\nRegras:\n- Responda exatamente à pergunta feita. Não repita o tutorial inteiro: traga só o trecho que resolve.\n- Quando houver um lugar no sistema, escreva o caminho do menu em negrito com o separador ›, por exemplo **Whatsapp › Disparos**.\n- Passos vão em lista numerada, uma ação por passo. Nomes de botões e telas em **negrito**, exatamente como estão nos tutoriais.\n- Se a resposta não estiver nos tutoriais, diga que não encontrou essa informação na Central de Ajuda e sugira falar com o suporte pelo botão \"Falar com o suporte\". Nunca invente telas, caminhos, prazos ou regras.\n- Não dê orientação clínica. Se a pessoa enviar dados de pacientes, não os repita e lembre que não deve compartilhá-los aqui.\n- Não cite fornecedores ou parceiros externos pelo nome; o módulo se chama Communicare Conversas.\n- Seja breve: no máximo uns 150 palavras, salvo quando o passo a passo exigir mais.\n- Na última linha, escreva FONTES: seguido dos números dos tutoriais que você usou, separados por vírgula (ex.: FONTES: 2, 5). Se não usou nenhum, escreva FONTES: nenhuma.";
const STOP = new Set(["de", "da", "do", "das", "dos", "e", "o", "a", "os", "as", "um", "uma", "como", "para", "no", "na", "em", "que", "eu", "meu", "minha", "por", "com", "nao"]);
const norm = (s) => (s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();

function selecionar(kb, texto, max) {
  const termos = norm(texto).split(/[^a-z0-9]+/).filter((t) => t.length > 2 && !STOP.has(t));
  return kb.map((d) => {
    const tit = norm(d.titulo + " " + d.caminho), corpo = norm(d.conteudo);
    let pts = 0;
    for (const t of termos) {
      const r = t.length > 4 ? t.slice(0, -1) : t;
      if (tit.includes(r)) pts += 4;
      pts += Math.min(corpo.split(r).length - 1, 4);
    }
    return { d, pts };
  }).filter((x) => x.pts > 0).sort((a, b) => b.pts - a.pts).slice(0, max).map((x) => x.d);
}

async function carregarKB(env, ctx) {
  const cache = caches.default;
  const req = new Request(env.KB_URL);
  let res = await cache.match(req);
  if (!res) {
    res = await fetch(env.KB_URL, { cf: { cacheTtl: 600 } });
    if (!res.ok) throw new Error("kb " + res.status);
    const copia = new Response(res.clone().body, res);
    copia.headers.set("Cache-Control", "max-age=600");
    ctx.waitUntil(cache.put(req, copia));
  }
  return res.json();
}

function cors(env, extra = {}) {
  return {
    "Access-Control-Allow-Origin": env.ALLOWED_ORIGIN,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "content-type",
    "Vary": "Origin",
    ...extra,
  };
}

const json = (env, obj, status = 200) =>
  new Response(JSON.stringify(obj), { status, headers: cors(env, { "content-type": "application/json; charset=utf-8" }) });

export default {
  async fetch(request, env, ctx) {
    if (request.method === "OPTIONS") return new Response(null, { headers: cors(env) });
    if (request.method !== "POST") return json(env, { erro: "método não permitido" }, 405);
    if (request.headers.get("Origin") !== env.ALLOWED_ORIGIN) return json(env, { erro: "origem não permitida" }, 403);

    let body;
    try { body = await request.json(); } catch { return json(env, { erro: "corpo inválido" }, 400); }
    const pergunta = String(body.pergunta || "").trim().slice(0, 500);
    const historico = (Array.isArray(body.historico) ? body.historico : []).slice(-3)
      .map((h) => ({ p: String(h.p || "").slice(0, 500), r: String(h.r || "").slice(0, 1500) }));
    if (!pergunta) return json(env, { erro: "pergunta vazia" }, 400);

    let kb;
    try { kb = await carregarKB(env, ctx); } catch { return json(env, { erro: "base indisponível" }, 502); }

    const base = historico.map((h) => h.p).slice(-2).join(" ") + " " + pergunta;
    const docs = selecionar(kb, base, 4);
    const tutoriais = docs.map((d, n) =>
      `<tutorial numero="${n + 1}" titulo="${d.titulo}" onde_fica="${d.caminho}" quem_pode="${d.perfis}">\n${d.conteudo}\n</tutorial>`).join("\n");
    const conversa = historico.map((h) => `Pessoa: ${h.p}\nAssistente: ${h.r}`).join("\n\n");
    const conteudo = `<tutoriais>\n${tutoriais || "(nenhum tutorial relacionado)"}\n</tutoriais>\n\n` +
      (conversa ? `<conversa_anterior>\n${conversa}\n</conversa_anterior>\n\n` : "") + `Pergunta atual: ${pergunta}`;

    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json" },
      body: JSON.stringify({ model: env.MODEL || "claude-haiku-5-5", max_tokens: 700, system: PROMPT_IA, messages: [{ role: "user", content: conteudo }] }),
    });
    if (!r.ok) return json(env, { erro: "falha ao gerar resposta" }, 502);
    const out = await r.json();
    const texto = (out.content || []).filter((c) => c.type === "text").map((c) => c.text).join("").trim();

    const m = texto.match(/FONTES:\s*([^\n]*)\s*$/i);
    const resposta = m ? texto.slice(0, m.index).trim() : texto;
    const fontes = [];
    for (const n of (m ? m[1].match(/\d+/g) || [] : [])) {
      const d = docs[Number(n) - 1];
      if (d && !fontes.some((f) => f.u === d.url)) fontes.push({ t: d.titulo, u: d.url });
    }
    return json(env, { resposta, fontes });
  },
};
