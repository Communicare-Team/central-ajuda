(function () {
  // Base relativa: o script sabe onde está e calcula a raiz do site a partir dele.
  var src = document.currentScript.getAttribute('src');
  var raiz = src.replace(/assets\/site\.js$/, '');
  var SUFIXO = window.LINK_SUFIXO || '';

  function norm(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var STOP = { de: 1, da: 1, do: 1, das: 1, dos: 1, e: 1, o: 1, a: 1, os: 1, as: 1, um: 1, uma: 1, como: 1, para: 1, no: 1, na: 1, em: 1, que: 1, eu: 1, meu: 1, minha: 1, por: 1, com: 1, nao: 1 };

  // ---------- busca por palavras (instantânea) ----------
  function buscar(q, max) {
    var termos = norm(q).split(/[^a-z0-9]+/).filter(function (t) { return t.length > 1 && !STOP[t]; });
    if (!termos.length) return [];
    return (window.SEARCH_INDEX || []).map(function (d) {
      var tit = norm(d.t), pts = 0, achou = 0;
      termos.forEach(function (t) {
        var r = t.length > 4 ? t.slice(0, t.length - 1) : t; // tolera plural/singular
        if (tit.indexOf(r) > -1) { pts += 5; achou++; }
        else if (d.n.indexOf(r) > -1) { pts += 1; achou++; }
      });
      return { d: d, p: achou === termos.length ? pts + 3 : pts * 0.5 };
    }).filter(function (r) { return r.p > 0; })
      .sort(function (a, b) { return b.p - a.p; }).slice(0, max || 8);
  }

  // ---------- resposta com IA ----------
  var iaPronta = !!window.CHAT_ENDPOINT, sample = null, ocupado = false, historico = [];

  function selecionar(texto, max) {
    var termos = norm(texto).split(/[^a-z0-9]+/).filter(function (t) { return t.length > 2 && !STOP[t]; });
    return (window.KB || []).map(function (d) {
      var tit = norm(d.t + ' ' + d.c), corpo = norm(d.md), pts = 0;
      termos.forEach(function (t) {
        var r = t.length > 4 ? t.slice(0, t.length - 1) : t;
        if (tit.indexOf(r) > -1) pts += 4;
        pts += Math.min(corpo.split(r).length - 1, 4);
      });
      return { d: d, p: pts };
    }).filter(function (x) { return x.p > 0; })
      .sort(function (a, b) { return b.p - a.p; }).slice(0, max);
  }

  function montarPrompt(pergunta) {
    var base = historico.map(function (h) { return h.p; }).slice(-2).join(' ') + ' ' + pergunta;
    var docs = selecionar(base, 4);
    var ctx = docs.map(function (x, n) {
      return '<tutorial numero="' + (n + 1) + '" titulo="' + x.d.t + '" onde_fica="' + x.d.c + '" quem_pode="' + x.d.p + '">\n' + x.d.md + '\n</tutorial>';
    }).join('\n');
    var conversa = historico.slice(-3).map(function (h) { return 'Pessoa: ' + h.p + '\nAssistente: ' + h.r; }).join('\n\n');
    return {
      pergunta: pergunta, docs: docs,
      texto: window.PROMPT_IA + '\n\n<tutoriais>\n' + (ctx || '(nenhum tutorial relacionado)') + '\n</tutoriais>\n\n' +
        (conversa ? '<conversa_anterior>\n' + conversa + '\n</conversa_anterior>\n\n' : '') + 'Pergunta atual: ' + pergunta
    };
  }

  // Markdown mínimo e seguro: negrito, listas e parágrafos.
  function formatar(md) {
    var out = '', lista = null;
    function fecha() { if (lista) { out += '</' + lista + '>'; lista = null; } }
    esc(md).split('\n').forEach(function (l) {
      var t = l.trim().replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
      var mo = t.match(/^\d+[.)]\s+(.*)/), mu = t.match(/^[-•*]\s+(.*)/);
      if (mo) { if (lista !== 'ol') { fecha(); out += '<ol>'; lista = 'ol'; } out += '<li>' + mo[1] + '</li>'; }
      else if (mu) { if (lista !== 'ul') { fecha(); out += '<ul>'; lista = 'ul'; } out += '<li>' + mu[1] + '</li>'; }
      else if (!t) fecha();
      else { fecha(); out += '<p>' + t + '</p>'; }
    });
    fecha();
    return out;
  }

  function separarFontes(txt, docs) {
    var m = txt.match(/FONTES:\s*([^\n]*)\s*$/i);
    var limpo = m ? txt.slice(0, m.index).trim() : txt.replace(/FONTES:?[^\n]*$/i, '').trim();
    var usados = [];
    if (m) (m[1].match(/\d+/g) || []).forEach(function (n) { var d = docs[+n - 1]; if (d && usados.indexOf(d) < 0) usados.push(d); });
    return { texto: limpo, fontes: usados };
  }

  function chamarModelo(p, aoTexto) {
    if (window.CHAT_ENDPOINT) {
      return fetch(window.CHAT_ENDPOINT, {
        method: 'POST', headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ pergunta: p.pergunta, historico: historico.slice(-3) })
      }).then(function (r) { if (!r.ok) throw new Error('http ' + r.status); return r.json(); })
        .then(function (j) { p.fontesWorker = j.fontes || []; aoTexto(j.resposta); return j.resposta; });
    }
    return sample(p.texto, { cache: false, onText: function (ev) { aoTexto(ev.text); } }).then(function (r) { return r.text; });
  }

  function linkTut(u) { return raiz + u + SUFIXO; }

  // ---------- painel de resultado: resposta (esquerda) + artigos (direita) ----------
  function painelPara(box) {
    var p = document.getElementById('resultado-painel');
    if (!p) {
      p = document.createElement('div');
      p.id = 'resultado-painel';
      p.className = 'miolo resultado';
      p.setAttribute('aria-live', 'polite');
      var ancora = box.closest('.hero') || box;
      ancora.parentNode.insertBefore(p, ancora.nextSibling);
    }
    return p;
  }

  function listaArtigos(q) {
    var rs = buscar(q, 6);
    if (!rs.length) return '<p class="mini">Nenhum artigo encontrado com essas palavras.</p>';
    return rs.map(function (r) {
      return '<a class="art" href="' + linkTut(r.d.u) + '"><span class="r-t">' + esc(r.d.t) + '</span><span class="r-c">' + esc(r.d.c) + '</span></a>';
    }).join('');
  }

  function mostrarResultado(box, q) {
    var painel = painelPara(box);
    historico = [];
    painel.innerHTML =
      '<div class="res-grade' + (iaPronta ? '' : ' so-artigos') + '">' +
      (iaPronta ? '<section class="res-ia"><h2><span class="ia-selo">IA</span> Resposta</h2><div id="ia-trocas"></div></section>' : '') +
      '<aside class="res-artigos"><h2>Artigos relacionados</h2><div id="res-lista">' + listaArtigos(q) + '</div></aside></div>';
    painel.hidden = false;
    painel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    if (iaPronta) perguntar(q);
  }

  function perguntar(pergunta) {
    if (ocupado) return;
    ocupado = true;
    var trocas = document.getElementById('ia-trocas');
    var velho = trocas.querySelector('.ia-seguir');
    if (velho) velho.remove();
    var el = document.createElement('div');
    el.className = 'ia-troca';
    el.innerHTML = (historico.length ? '<p class="ia-pergunta">' + esc(pergunta) + '</p>' : '') +
      '<div class="ia-resposta"><p class="ia-pensando">Procurando nos tutoriais…</p></div>';
    trocas.appendChild(el);
    var alvo = el.querySelector('.ia-resposta');
    var p = montarPrompt(pergunta);
    chamarModelo(p, function (txt) { alvo.innerHTML = formatar(separarFontes(txt || '', p.docs).texto); })
      .then(function (final) {
        var r = separarFontes(final || '', p.docs);
        var fontes = p.fontesWorker ? p.fontesWorker.map(function (f) { return { href: f.u, t: f.t }; })
          : r.fontes.map(function (x) { return { href: linkTut(x.d.u), t: x.d.t }; });
        alvo.innerHTML = formatar(r.texto) + (fontes.length ? '<div class="ia-fontes"><span class="rotulo">Baseado em</span>' +
          fontes.map(function (f) { return '<a href="' + esc(f.href) + '">' + esc(f.t) + '</a>'; }).join('') + '</div>' : '');
        historico.push({ p: pergunta, r: r.texto });
        if (historico.length > 1) document.getElementById('res-lista').innerHTML = listaArtigos(pergunta);
      })
      .catch(function () {
        alvo.innerHTML = '<p>Não consegui gerar a resposta agora. Veja os artigos relacionados ao lado ou fale com o suporte.</p>';
      })
      .then(function () {
        ocupado = false;
        var f = document.createElement('form');
        f.className = 'ia-seguir';
        f.innerHTML = '<label for="ia-seguir-q" class="ia-rotulo">Ficou alguma dúvida? Pergunte em cima desta resposta.</label>' +
          '<div class="ia-linha"><input id="ia-seguir-q" type="text" maxlength="500" autocomplete="off" placeholder="Ex.: e se eu errar, consigo desfazer?"><button type="submit">Perguntar</button></div>' +
          '<p class="mini">Resposta gerada por IA a partir dos tutoriais da Central. Não informe dados de pacientes.</p>';
        f.addEventListener('submit', function (e) { e.preventDefault(); var v = f.querySelector('input').value.trim(); if (v) perguntar(v); });
        trocas.appendChild(f);
      });
  }

  // ---------- caixa de busca única ----------
  document.querySelectorAll('.busca').forEach(function (box) {
    var input = box.querySelector('input'), out = box.querySelector('.resultados'), sel = -1;
    function render() {
      var q = input.value.trim();
      if (q.length < 2) { out.hidden = true; return; }
      var rs = buscar(q, 6); sel = -1;
      var dica = '<div class="r-dica">Aperte <kbd>Enter</kbd> para ver ' + (iaPronta ? 'a resposta completa com IA' : 'todos os resultados') + '</div>';
      out.innerHTML = dica + (rs.length ? rs.map(function (r) {
        return '<a href="' + linkTut(r.d.u) + '"><span class="r-t">' + esc(r.d.t) + '</span><span class="r-c">' + esc(r.d.s) + ' · ' + esc(r.d.c) + '</span></a>';
      }).join('') : '');
      out.hidden = false;
    }
    input.addEventListener('input', render);
    input.addEventListener('keydown', function (e) {
      var links = out.querySelectorAll('a');
      if (e.key === 'Enter') {
        e.preventDefault();
        if (sel >= 0 && links[sel]) { links[sel].click(); return; }
        var q = input.value.trim();
        if (q.length < 2) return;
        out.hidden = true;
        mostrarResultado(box, q);
      } else if ((e.key === 'ArrowDown' || e.key === 'ArrowUp') && links.length) {
        e.preventDefault();
        sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + links.length) % links.length;
        links.forEach(function (l, i) { l.classList.toggle('sel', i === sel); });
      } else if (e.key === 'Escape') { out.hidden = true; }
    });
    var btn = box.querySelector('.busca-btn');
    if (btn) btn.addEventListener('click', function () {
      var q = input.value.trim();
      if (q.length < 2) { input.focus(); return; }
      out.hidden = true;
      mostrarResultado(box, q);
    });
    document.addEventListener('click', function (e) { if (!box.contains(e.target)) out.hidden = true; });
  });

  // Liga a IA: Worker em produção; na prévia, a IA do Claude (se o visitante autorizar).
  function atualizarPlaceholder() {
    document.querySelectorAll('.busca input').forEach(function (i) {
      i.placeholder = 'Pergunte ou busque: por que minha mensagem foi cancelada?';
    });
  }
  if (iaPronta) atualizarPlaceholder();
  else if (window.claude && window.claude.use) {
    window.claude.use('sample').then(function (s) { if (s) { sample = s; iaPronta = true; atualizarPlaceholder(); } }).catch(function () {});
  }
})();

(function () {
  var btn = document.getElementById("btn-tema");
  if (!btn) return;
  btn.addEventListener("click", function () {
    var escuro = document.documentElement.dataset.theme !== "dark";
    if (escuro) document.documentElement.dataset.theme = "dark";
    else delete document.documentElement.dataset.theme;
    try { localStorage.setItem("tema", escuro ? "escuro" : "claro"); } catch (e) {}
  });
})();
