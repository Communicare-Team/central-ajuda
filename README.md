# Central de Ajuda da Communicare

Código que gera o site **ajuda.communicare.com.br** (tutoriais, Novidades e Mapa do sistema).

## Como funciona

- `content/tutoriais/*.md`: um arquivo por tutorial (cabeçalho com título, seção, caminho no menu, perfis e vídeo).
- `content/novidades.json`: itens do changelog de clientes. Só os com `"status": "Publicado"` aparecem em `/changelog`.
- `content/menu*.json` e `content/mapa-menu.json`: seções do site e Mapa do sistema.
- `assets/`: CSS, JS, logo e favicon.
- `build.py`: lê `content/` e gera o site em `dist/` (e uma prévia local em `previa/`).
- `worker/`: Cloudflare Worker da busca com IA (`ajuda-ia.communicare.com.br`). A chave da API fica nos segredos do Worker, nunca aqui.

## Publicação

Todo push no `main` roda o GitHub Action `Publicar Central de Ajuda`: gera o site e publica no projeto `central-ajuda` do Cloudflare Pages.
Segredos do repositório: `CLOUDFLARE_API_TOKEN` (permissão Cloudflare Pages: Edit) e `CLOUDFLARE_ACCOUNT_ID`.

## Rodar localmente

```bash
pip install -r requirements.txt
python build.py
```
