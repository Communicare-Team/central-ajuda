#!/usr/bin/env python3
"""Gerador estático da Central de Ajuda Communicare.

Lê content/ (tutoriais em Markdown, mapa do menu, novidades) e gera dist/,
pronto para subir no Cloudways. Todos os links são relativos, então o site
funciona em qualquer pasta e também aberto direto do disco.
"""
import datetime as dt
import html
import json
import re
import shutil
import unicodedata
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"
SITE_URL = "https://ajuda.communicare.com.br"

# Cole aqui o snippet do WebChat do Communicare Conversas quando tiver.
# Enquanto estiver vazio, o botão "Falar com o suporte" abre o aviso padrão.
WEBCHAT_LINK = "https://wshort.me/PHJQ"  # link público do widget "Ajuda"
# Widget de Atendimento "Suporte" (Communicare Conversas) — vai no <head>; botões com a classe h-widget-trigger abrem o chat
WEBCHAT_SNIPPET = '<script type="application/javascript" src="https://cdn.wts.chat/scripts/widget/v3/h-widget-min.js" data-widget="ajuda-25b062"></script>'

# URL do Cloudflare Worker que responde as perguntas com IA (produção).
# Vazio = a caixa usa a IA do próprio Claude (só funciona na prévia em artifact).
CHAT_ENDPOINT = "https://ajuda-ia.communicare.com.br"  # Worker da busca com IA (worker/worker.js)

# Instruções do assistente. São as mesmas na prévia e no Worker.
PROMPT_IA = """Você é o assistente da Central de Ajuda da Communicare, um sistema de gestão para clínicas e consultórios.
Responda em português do Brasil, de forma direta e cordial, usando SOMENTE os tutoriais fornecidos entre <tutoriais>.

Regras:
- Responda exatamente à pergunta feita. Não repita o tutorial inteiro: traga só o trecho que resolve.
- Quando houver um lugar no sistema, escreva o caminho do menu em negrito com o separador ›, por exemplo **Whatsapp › Disparos**.
- Passos vão em lista numerada, uma ação por passo. Nomes de botões e telas em **negrito**, exatamente como estão nos tutoriais.
- Se a resposta não estiver nos tutoriais, diga que não encontrou essa informação na Central de Ajuda e sugira falar com o suporte pelo botão "Falar com o suporte". Nunca invente telas, caminhos, prazos ou regras.
- Não dê orientação clínica. Se a pessoa enviar dados de pacientes, não os repita e lembre que não deve compartilhá-los aqui.
- Não cite fornecedores ou parceiros externos pelo nome; o módulo se chama Communicare Conversas.
- Seja breve: no máximo uns 150 palavras, salvo quando o passo a passo exigir mais.
- Na última linha, escreva FONTES: seguido dos números dos tutoriais que você usou, separados por vírgula (ex.: FONTES: 2, 5). Se não usou nenhum, escreva FONTES: nenhuma."""

SECOES = [
    ("inicie-na-plataforma", "Inicie na plataforma", "Primeiro acesso, configurações iniciais e trilhas por perfil"),
    ("agendamentos-e-consultas", "Agendamentos e consultas", "Agenda, sala de espera, filas, prontuário e teleconsulta"),
    ("configuracoes-para-profissionais", "Configurações para profissionais", "Seus horários, modelos, impressos e procedimentos"),
    ("configuracoes-do-gestor", "Configurações do gestor", "Clínicas, usuários, permissões, agenda online e mensageria"),
    ("financeiro-e-faturamento", "Financeiro e faturamento", "Recebimentos, notas fiscais, pacotes, TISS e Asaas"),
    ("relatorios-e-analises", "Relatórios e análises", "Relatórios administrativos, financeiros e dashboards"),
    ("funcionalidades-avancadas", "Funcionalidades avançadas", "Gestão de cuidados, formulários e teleinterconsulta"),
    ("assinatura-e-suporte", "Assinatura e suporte", "Plano, faturas e como falar com a gente"),
    ("communicare-conversas", "Communicare Conversas", "Atendimento por WhatsApp, Instagram e Messenger"),
]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]


# ---------- utilidades ----------
def esc(s):
    return html.escape(s or "", quote=True)


def norm(s):
    s = unicodedata.normalize("NFD", s or "").lower()
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def data_br(iso):
    d = dt.date.fromisoformat(iso)
    return f"{d.day:02d}/{d.month:02d}/{d.year}"


def parse_md(path):
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    meta["corpo"] = m.group(2).strip()
    return meta


def secoes_md(corpo):
    """Divide o corpo em [(titulo_h2, markdown)]."""
    partes = re.split(r"^## (.+)$", corpo, flags=re.M)
    return [(partes[i].strip(), partes[i + 1].strip()) for i in range(1, len(partes), 2)]


MD = markdown.Markdown(extensions=["sane_lists", "tables"])


def md2html(s):
    MD.reset()
    return MD.convert(s)


def caminho_html(caminho):
    partes = [p.strip() for p in caminho.split("›")]
    return '<span class="sep" aria-hidden="true">›</span>'.join(
        f'<span class="crumb">{esc(p)}</span>' for p in partes)


def loom_embed(url):
    m = re.search(r"loom\.com/share/([0-9a-f]{32})(?:\?t=(\d+))?", url or "")
    if not m:
        return None
    u = f"https://www.loom.com/embed/{m.group(1)}?hide_owner=true&hide_share=true&hide_title=true"
    if m.group(2):
        u += f"&t={m.group(2)}"
    return u


# ---------- layout ----------
def pagina(titulo, corpo, prof, descricao="", ativo=None):
    r = "../" * prof
    nav = [("", "Início"), ("tutoriais/", "Tutoriais"), ("changelog/", "Novidades"), ("mapa-do-menu/", "Mapa do sistema")]
    links = "".join(
        f'<a href="{r}{href}" class="{"on" if ativo == href else ""}">{rot}</a>' for href, rot in nav)
    titulo_full = f"{titulo} · Central de Ajuda Communicare" if titulo else "Central de Ajuda Communicare"
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo_full)}</title>
<meta name="description" content="{esc(descricao)}">
<meta name="robots" content="noindex">
<link rel="icon" href="{r}assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
<script>try{{if(localStorage.getItem("tema")==="escuro")document.documentElement.dataset.theme="dark"}}catch(e){{}}</script>
{WEBCHAT_SNIPPET}
</head>
<body>
<header class="topo">
  <div class="topo-in">
    <a href="{r}" class="marca"><img src="{r}assets/logo.png" alt="Communicare" height="30"><span>Central de Ajuda</span></a>
    <nav class="nav">{links}</nav>
    <button type="button" class="tema" id="btn-tema" aria-label="Alternar tema claro/escuro" title="Tema claro/escuro"><svg class="ico-lua" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M20 15.3A8 8 0 0 1 8.7 4a8 8 0 1 0 11.3 11.3Z"/></svg><svg class="ico-sol" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><circle cx="12" cy="12" r="4.5" fill="currentColor"/><path stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  </div>
</header>
<main>
{corpo}
</main>
<footer class="rodape">
  <div class="rodape-in">
    <p><strong>Não encontrou o que procurava?</strong> <button type="button" class="link-chat h-widget-trigger">Fale com o nosso suporte pelo chat</button>.</p>
    <p class="mini">Communicare · A plataforma completa para a gestão da jornada do paciente · <a href="https://communicare.com.br">communicare.com.br</a></p>
  </div>
</footer>
<button type="button" class="suporte h-widget-trigger" id="btn-suporte" aria-label="Falar com o suporte">
  <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M12 3C6.5 3 2 6.9 2 11.7c0 2.4 1.1 4.6 3 6.2L4.3 21l3.6-1.7c1.3.4 2.7.6 4.1.6 5.5 0 10-3.9 10-8.7S17.5 3 12 3Z"/></svg>
  <span>Falar com o suporte</span>
</button>
<script src="{r}assets/search-index.js"></script>
<script src="{r}assets/kb.js"></script>
<script src="{r}assets/site.js"></script>
</body>
</html>"""


def busca_html(placeholder="Digite sua dúvida, por exemplo: transferir conversa"):
    return f"""<div class="busca" role="search">
  <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M10.5 3a7.5 7.5 0 0 1 5.9 12.1l4.2 4.3-1.4 1.4-4.3-4.2A7.5 7.5 0 1 1 10.5 3Zm0 2a5.5 5.5 0 1 0 0 11 5.5 5.5 0 0 0 0-11Z"/></svg>
  <input id="q" type="search" placeholder="{esc(placeholder)}" autocomplete="off" aria-label="Buscar na Central de Ajuda">
  <button type="button" class="busca-btn">Buscar</button>
  <div id="resultados" class="resultados" hidden></div>
</div>"""


def ia_html():
    return """<form class="ia" id="ia-form" hidden>
  <label for="ia-q" class="ia-rotulo"><span class="ia-selo">IA</span> Ou pergunte com suas palavras e receba uma resposta pronta</label>
  <div class="ia-linha">
    <input id="ia-q" type="text" maxlength="500" autocomplete="off" placeholder="Ex.: por que minha mensagem de confirmação foi cancelada?">
    <button type="submit" id="ia-enviar">Perguntar</button>
  </div>
</form>"""


# ---------- geração ----------
def carregar_tutoriais():
    tuts = [parse_md(p) for p in sorted((CONTENT / "tutoriais").glob("*.md"))]
    for t in tuts:
        t["ordem"] = int(t.get("ordem") or 99)
        t["secs"] = secoes_md(t["corpo"])
    return sorted(tuts, key=lambda t: (t["secao"], t["ordem"]))


def render_tutorial(t, irmaos, secao_nome):
    prof = 2
    r = "../" * prof
    ignorar = {"Quem pode fazer", "Onde fica", "Perguntas frequentes"}
    blocos = []
    for tit, md in t["secs"]:
        if tit in ignorar:
            continue
        blocos.append(f'<section><h2 id="{esc(norm(tit).replace(" ", "-"))}">{esc(tit)}</h2>{md2html(md)}</section>')
    faq = dict(t["secs"]).get("Perguntas frequentes", "")
    faq_html = ""
    if faq:
        itens = re.split(r"^### (.+)$", faq, flags=re.M)
        qs = "".join(
            f"<details><summary>{esc(itens[i].strip())}</summary>{md2html(itens[i + 1].strip())}</details>"
            for i in range(1, len(itens), 2))
        faq_html = f'<section class="faq"><h2 id="perguntas-frequentes">Perguntas frequentes</h2>{qs}</section>'
    emb = loom_embed(t.get("video"))
    video_html = ""
    if emb:
        video_html = f"""<section class="video"><h2>Prefere ver em vídeo?</h2>
<div class="video-box"><iframe src="{esc(emb)}" loading="lazy" allowfullscreen title="{esc(t.get('video_rotulo'))}"></iframe></div>
<p class="mini">{esc(t.get('video_rotulo'))}</p></section>"""
    lateral = "".join(
        f'<li><a href="{r}tutoriais/{i["slug"]}/" class="{"on" if i is t else ""}">{esc(i["titulo"])}</a></li>'
        for i in irmaos)
    corpo = f"""<div class="miolo com-lateral">
<aside class="lateral"><p class="lateral-tit"><a href="{r}secoes/{t['secao']}/">{esc(secao_nome)}</a></p><ul>{lateral}</ul></aside>
<article class="artigo">
  <nav class="trilha"><a href="{r}">Início</a> › <a href="{r}secoes/{t['secao']}/">{esc(secao_nome)}</a></nav>
  <h1>{esc(t['titulo'])}</h1>
  <div class="meta">
    <div class="meta-item"><span class="rotulo">Onde fica</span><div class="caminho">{caminho_html(t['caminho'])}</div></div>
    <div class="meta-item"><span class="rotulo">Quem pode fazer</span><p>{esc(t['perfis'])}</p></div>
  </div>
  {''.join(blocos)}
  {faq_html}
  {video_html}
  <p class="atualizado">Atualizado em {data_br(t['atualizado'])}</p>
</article>
</div>"""
    resumo = t["secs"][0][1] if t["secs"] else ""
    return pagina(t["titulo"], corpo, prof, re.sub(r"[*_]", "", resumo)[:160], "tutoriais/")


def card_tut(t, r):
    resumo = re.sub(r"[*_]", "", t["secs"][0][1]) if t["secs"] else ""
    return f"""<a class="card-tut" href="{r}tutoriais/{t['slug']}/"><h3>{esc(t['titulo'])}</h3>
<p>{esc(resumo[:140])}{'…' if len(resumo) > 140 else ''}</p><span class="caminho mini">{caminho_html(t['caminho'])}</span></a>"""


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "assets").mkdir(parents=True)
    for f in ["logo.png", "favicon.png", "style.css", "site.js"]:
        shutil.copy(ROOT / "assets" / f, DIST / "assets" / f)

    tuts = carregar_tutoriais()
    nomes = {s: n for s, n, _ in SECOES}
    por_secao = {s: [t for t in tuts if t["secao"] == s] for s, _, _ in SECOES}

    # tutoriais + versão .md
    for t in tuts:
        d = DIST / "tutoriais" / t["slug"]
        d.mkdir(parents=True)
        (d / "index.html").write_text(render_tutorial(t, por_secao[t["secao"]], nomes[t["secao"]]), encoding="utf-8")
        (d / "index.md").write_text(f"# {t['titulo']}\n\n{t['corpo']}\n", encoding="utf-8")

    # páginas de seção
    for s, nome, desc in SECOES:
        d = DIST / "secoes" / s
        d.mkdir(parents=True)
        lst = por_secao[s]
        itens = "".join(card_tut(t, "../../") for t in lst) or '<p class="vazio">Os tutoriais desta seção estão sendo escritos. Enquanto isso, use a busca ou fale com o suporte.</p>'
        corpo = f"""<div class="miolo"><nav class="trilha"><a href="../../">Início</a></nav>
<h1>{esc(nome)}</h1><p class="sub">{esc(desc)}</p><div class="grade-tut">{itens}</div></div>"""
        (d / "index.html").write_text(pagina(nome, corpo, 2, desc, "tutoriais/"), encoding="utf-8")

    # lista de todos os tutoriais
    d = DIST / "tutoriais"
    blocos = ""
    for s, nome, _ in SECOES:
        if por_secao[s]:
            blocos += f'<h2><a href="../secoes/{s}/">{esc(nome)}</a></h2><div class="grade-tut">{"".join(card_tut(t, "../") for t in por_secao[s])}</div>'
    corpo = f'<div class="miolo"><h1>Todos os tutoriais</h1>{busca_html()}{blocos}</div>'
    (d / "index.html").write_text(pagina("Tutoriais", corpo, 1, "Todos os tutoriais", "tutoriais/"), encoding="utf-8")

    # home
    cards = ""
    for s, nome, desc in sorted(SECOES, key=lambda x: not por_secao[x[0]]):
        n = len(por_secao[s])
        selo = f"{n} tutoria{'is' if n != 1 else 'l'}" if n else "Em breve"
        cards += f"""<a class="card-secao{' vazia' if not n else ''}" href="secoes/{s}/"><h3>{esc(nome)}</h3><p>{esc(desc)}</p><span class="selo">{selo}</span></a>"""
    recentes = sorted(tuts, key=lambda t: t["atualizado"], reverse=True)[:4]
    corpo = f"""<section class="hero"><div class="hero-in">
<h1>Como podemos ajudar?</h1>
<p>Tutoriais passo a passo, com o caminho exato no menu do sistema.</p>
{busca_html()}
</div></section>
<div class="miolo">
<h2 class="titulo-secao">Navegue por assunto</h2>
<div class="grade-secoes">{cards}</div>
<h2 class="titulo-secao">Atualizados recentemente</h2>
<div class="grade-tut">{''.join(card_tut(t, '') for t in recentes)}</div>
</div>"""
    (DIST / "index.html").write_text(pagina("", corpo, 0, "Central de Ajuda da Communicare: tutoriais, novidades e mapa do sistema.", ""), encoding="utf-8")

    build_mapa()
    build_changelog()

    # índice de busca (JS, funciona até aberto do disco)
    idx = []
    for t in tuts:
        perguntas = re.findall(r"^### (.+)$", t["corpo"], flags=re.M)
        texto = re.sub(r"[#*_>`-]", " ", t["corpo"])
        idx.append({"t": t["titulo"], "u": f"tutoriais/{t['slug']}/", "c": t["caminho"], "s": nomes[t["secao"]],
                    "q": perguntas, "n": norm(t["titulo"] + " " + t["caminho"] + " " + " ".join(perguntas) + " " + texto)})
    (DIST / "assets" / "search-index.js").write_text("window.SEARCH_INDEX=" + json.dumps(idx, ensure_ascii=False) + ";", encoding="utf-8")
    kb = [{"t": t["titulo"], "u": f"tutoriais/{t['slug']}/", "c": t["caminho"], "p": t["perfis"], "md": t["corpo"]} for t in tuts]
    (DIST / "assets" / "kb.js").write_text(
        "window.KB=" + json.dumps(kb, ensure_ascii=False) + ";window.PROMPT_IA=" + json.dumps(PROMPT_IA, ensure_ascii=False)
        + ";window.CHAT_ENDPOINT=" + json.dumps(CHAT_ENDPOINT) + ";", encoding="utf-8")
    worker = (ROOT / "worker" / "worker.template.js").read_text(encoding="utf-8")
    (ROOT / "worker" / "worker.js").write_text(worker.replace("__PROMPT_IA__", json.dumps(PROMPT_IA, ensure_ascii=False)), encoding="utf-8")

    # base para o chat de IA (etapa 2) e llms.txt
    base = [{"titulo": t["titulo"], "url": f"{SITE_URL}/tutoriais/{t['slug']}/", "secao": nomes[t["secao"]],
             "caminho": t["caminho"], "perfis": t["perfis"], "conteudo": t["corpo"], "atualizado": t["atualizado"]} for t in tuts]
    (DIST / "base.json").write_text(json.dumps(base, ensure_ascii=False, indent=1), encoding="utf-8")
    llms = ["# Central de Ajuda Communicare", "", "> Tutoriais da plataforma Communicare, com o caminho exato no menu.", ""]
    for s, nome, _ in SECOES:
        if por_secao[s]:
            llms.append(f"## {nome}")
            llms += [f"- [{t['titulo']}]({SITE_URL}/tutoriais/{t['slug']}/index.md): Onde fica: {t['caminho']}" for t in por_secao[s]]
            llms.append("")
    llms += ["## Outros", f"- [Mapa do sistema]({SITE_URL}/mapa-do-menu/): todos os itens do menu e quem vê cada um",
             f"- [Novidades]({SITE_URL}/changelog/): histórico de mudanças do produto"]
    (DIST / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")
    (DIST / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    print(f"ok: {len(tuts)} tutoriais, {sum(1 for _ in DIST.rglob('*.html'))} páginas")


def build_mapa():
    mapa = json.loads((CONTENT / "mapa-menu.json").read_text(encoding="utf-8"))
    linhas_por_grupo = {}
    for it in mapa["itens"]:
        grupo = it["caminho"].split(" › ")[0]
        if " › " not in it["caminho"]:
            grupo = "Telas principais"
        linhas_por_grupo.setdefault(grupo, []).append(it)
    blocos = ""
    for grupo, its in linhas_por_grupo.items():
        nota = mapa["notas_grupo"].get(grupo, "")
        linhas = "".join(
            f"<tr><td><div class='caminho'>{caminho_html(i['caminho'])}</div></td><td>{esc(' · '.join(i['abas'])) or '—'}</td><td>{esc(i['quem'])}</td></tr>"
            for i in its)
        blocos += f"""<section class="grupo-mapa"><h2>{esc(grupo)}</h2>{f'<p class="sub">{esc(nota)}</p>' if nota else ''}
<div class="tabela-rolagem"><table><thead><tr><th>Caminho no menu</th><th>Abas na tela</th><th>Quem vê</th></tr></thead><tbody>{linhas}</tbody></table></div></section>"""
    legenda = "".join(f"<li><strong>{esc(k)}:</strong> {esc(v)}</li>" for k, v in mapa["legenda"].items())
    cond = "".join(f"<li><strong>{esc(k)}:</strong> {esc(v)}</li>" for k, v in mapa["condicionais"].items())
    corpo = f"""<div class="miolo"><nav class="trilha"><a href="../">Início</a></nav>
<h1>Mapa do sistema</h1>
<p class="sub">Todos os itens do menu lateral, com as abas de cada tela e quem consegue ver cada um. Use para descobrir onde fica uma função.</p>
<div class="caixa"><h3>Quem vê cada item</h3><ul>{legenda}</ul></div>
{blocos}
<div class="caixa"><h3>Itens que só aparecem em algumas contas</h3><ul>{cond}</ul></div>
<p class="atualizado">Atualizado em {data_br(mapa['atualizado'])}</p></div>"""
    d = DIST / "mapa-do-menu"
    d.mkdir()
    (d / "index.html").write_text(pagina("Mapa do sistema", corpo, 1, "Onde fica cada função no menu da Communicare", "mapa-do-menu/"), encoding="utf-8")


# Rótulo exibido para cada tipo do database Novidades (Heitor, 09/11: "Ajuste" aparece como "Correção").
ROTULO_TIPO = {"Ajuste": "Correção"}


def build_changelog():
    itens = json.loads((CONTENT / "novidades.json").read_text(encoding="utf-8"))
    itens = [i for i in itens if i.get("status") == "Publicado"]
    edicoes = {}
    for i in itens:
        edicoes.setdefault(i["edicao"], []).append(i)
    base = DIST / "changelog"
    base.mkdir()
    lista = ""
    mes_atual = None
    for ed in sorted(edicoes, reverse=True):
        its = sorted(edicoes[ed], key=lambda i: i.get("ordem", 99))
        d = dt.date.fromisoformat(ed)
        mes = f"{MESES[d.month - 1].capitalize()} de {d.year}"
        destaque = next((i["destaque"] for i in its if i.get("destaque")), its[0]["titulo"])
        if mes != mes_atual:
            lista += f"<h2>{mes}</h2>"
            mes_atual = mes
        lista += f'<a class="card-tut" href="{ed}/"><h3>{data_br(ed)} - {esc(destaque)}</h3><p>{len(its)} novidade{"s" if len(its) > 1 else ""}</p></a>'
        # página da edição: blocos por módulo
        por_mod = {}
        for i in its:
            por_mod.setdefault(i["modulo"], []).append(i)
        blocos = ""
        for mod, ms in por_mod.items():
            li = "".join(
                f"<div class='novidade'><h3>{esc(m['titulo'])} <span class='tipo'>{esc(ROTULO_TIPO.get(m.get('tipo',''), m.get('tipo','')))}</span></h3><p>{esc(m['texto'])}</p>"
                + (f"<a href='{esc(m['tutorial'])}'>Ver tutorial</a>" if (m.get("tutorial") or "").startswith(SITE_URL) else "") + "</div>" for m in ms)
            blocos += f"<section><h2>{esc(mod)}</h2>{li}</section>"
        de = base / ed
        de.mkdir()
        corpo = f"""<div class="miolo estreito"><nav class="trilha"><a href="../../">Início</a> › <a href="../">Novidades</a> › {mes}</nav>
<h1>{data_br(ed)} - {esc(destaque)}</h1>{blocos}</div>"""
        (de / "index.html").write_text(pagina(f"Novidades {data_br(ed)}", corpo, 2, destaque, "changelog/"), encoding="utf-8")
    if not lista:
        lista = '<div class="vazio"><p><strong>A primeira edição chega em breve.</strong></p><p>Toda semana publicamos aqui as novidades, melhorias e ajustes da plataforma, organizados por módulo.</p></div>'
    corpo = f"""<div class="miolo estreito"><nav class="trilha"><a href="../">Início</a></nav>
<h1>Novidades de produto</h1><p class="sub">O que mudou na Communicare, semana a semana.</p>{lista}</div>"""
    (base / "index.html").write_text(pagina("Novidades", corpo, 1, "Novidades de produto da Communicare", "changelog/"), encoding="utf-8")
    build_novidades_app(edicoes)


# Tipo no arquivo lido pelo modal do app (DCC-7588): Novidade e Melhoria → "novidade".
TIPO_APP = {"Novidade": "novidade", "Melhoria": "novidade", "Desempenho": "desempenho", "Ajuste": "ajuste"}


def build_novidades_app(edicoes):
    """Gera /novidades/index.json e /novidades/AAAA-MM-DD.json, lidos pelo modal de Novidades do app.

    Só entram edições com resumo para o modal (a partir de 10/11/2026); as anteriores ficam só na página.
    O _headers libera a leitura pelo app (CORS) e evita cache longo.
    """
    pasta = DIST / "novidades"
    pasta.mkdir()
    datas = []
    for ed in sorted(edicoes, reverse=True):
        its = sorted(edicoes[ed], key=lambda i: i.get("ordem", 99))
        if not any(i.get("resumo") for i in its):
            continue
        destaque = next((i["destaque"] for i in its if i.get("destaque")), its[0]["titulo"])
        dados = {"edicao": ed, "destaque": destaque, "itens": [
            {"tipo": TIPO_APP.get(i.get("tipo"), "novidade"), "modulo": i["modulo"], "titulo": i["titulo"],
             "resumo": i.get("resumo") or i["texto"], "texto": i["texto"],
             "tutorial": i["tutorial"] if (i.get("tutorial") or "").startswith(SITE_URL) else None}
            for i in its]}
        (pasta / f"{ed}.json").write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
        datas.append(ed)
    (pasta / "index.json").write_text(json.dumps({"ultima": datas[0] if datas else None, "edicoes": datas},
                                                 ensure_ascii=False, indent=2), encoding="utf-8")
    (DIST / "_headers").write_text("/novidades/*\n  Access-Control-Allow-Origin: *\n  Cache-Control: public, max-age=300\n", encoding="utf-8")


def gerar_previa():
    """Cópia de dist/ com links terminando em index.html, para abrir sem servidor."""
    prev = ROOT / "previa"
    if prev.exists():
        shutil.rmtree(prev)
    shutil.copytree(DIST, prev)
    for f in prev.rglob("*.html"):
        h = f.read_text(encoding="utf-8")
        h = re.sub(r'href="((?:\.\./)*[^"#:]*?/)"', r'href="\1index.html"', h)
        h = h.replace('href=""', 'href="index.html"')
        h = h.replace(WEBCHAT_SNIPPET, "")
        h = re.sub(r'<button type="button" class="([^"]*)h-widget-trigger"([^>]*)>(.*?)</button>',
                   lambda m: f'<a class="{m.group(1).strip()}"{m.group(2)} href="{WEBCHAT_LINK}" target="_blank" rel="noopener">{m.group(3)}</a>', h, flags=re.S)
        f.write_text(h, encoding="utf-8")
    js = prev / "assets" / "site.js"
    js.write_text(js.read_text(encoding="utf-8").replace("window.LINK_SUFIXO || ''", "'index.html'"), encoding="utf-8")


if __name__ == "__main__":
    build()
    gerar_previa()
