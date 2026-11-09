---
titulo: Como criar um chatbot de atendimento
slug: como-criar-um-chatbot-de-atendimento
secao: communicare-conversas
ordem: 21
perfis: Administrador da conta
caminho: Conversas › Apps › Chatbot
video: 
video_rotulo: 
atualizado: 2026-11-05
---
## Para que serve

Responder automaticamente quem escreve para a clínica: dar boas-vindas, oferecer um menu (marcar, remarcar, cancelar, dúvidas), coletar informações e encaminhar o paciente para a equipe certa, a qualquer hora.

## Quem pode fazer

Só usuário com perfil **Administrador** no Conversas cria, altera e arquiva chatbots.

## Onde fica

Botão verde **Conversas** no topo do sistema › **Apps** › **Chatbot**.

## Antes de começar

- Configure o horário de atendimento: ele decide se o chatbot "dentro do horário" ou "fora do horário" vai responder.
- Crie as equipes que vão receber os pacientes encaminhados pelo bot.
- Desenhe o caminho antes, no papel: para onde cada resposta leva o paciente.

## Tipos de chatbot

- **Atendimento:** responde quem escreve no canal, com gatilhos por horário ou palavra-chave.
- **Automação:** usado em campanhas, sequências e mensagens agendadas, ou iniciado manualmente na conversa pelo **clipe** › **Iniciar chatbot**.

## Passo a passo

1. Em **Chatbot**, escolha o tipo **Atendimento** e clique em **+ Novo**.
2. Informe o nome, o tipo de canal (WhatsApp oficial, Instagram, Messenger ou WebChat) e a equipe padrão. Salve.
3. No editor, clique em **+** para montar o fluxo com blocos:
   - **Mensagem:** texto, áudio, imagem, vídeo ou PDF.
   - **Pergunta:** com texto, botões ou lista; o bot espera a resposta.
   - **Condicionais:** caminhos diferentes conforme a resposta, a etiqueta, o horário ou o dia da semana.
   - **Ações:** adicionar etiqueta, **encaminhar para equipe**, encerrar atendimento, ir para outro chatbot.
4. Clique em **Salvar alterações**.
5. Para testar, clique em **Testar** › **Publicar alterações**. O sistema gera um código com #. Envie esse código pelo canal: o bot responde só para você.
6. Quando estiver tudo certo, clique em **Publicar versão**.
7. Defina o gatilho: **Iniciar atendimento pelo canal** (qualquer horário), **Dentro do horário**, **Fora do horário** ou **Palavra-chave**.

## Regras importantes

- O tipo de canal não pode ser mudado depois de criado.
- Testar não coloca o bot em uso. Só **Publicar versão** faz isso.
- O gatilho "pelo canal" não convive com "dentro/fora do horário": ao escolher um, o outro sai.
- Se o canal já tiver outro bot no mesmo gatilho, aparece **Conflito de chatbot** ao publicar.
- A Meta exige que o bot ofereça um caminho fácil para o paciente falar com uma pessoa. Inclua sempre a opção de encaminhar para a equipe.
- Para aproveitar um bot pronto, use **Duplicar** ou copie e cole blocos entre chatbots.
- O agente de IA no atendimento é contratado à parte — fale com o suporte.

## Perguntas frequentes

- **Publiquei e o bot não responde.** Confira se há gatilho ligado ao canal, se a versão foi publicada (não só testada) e se não há outro bot no mesmo gatilho.
- **O bot de fora do horário respondeu durante o expediente.** Revise o horário de atendimento e o fuso.
- **Arquivei um bot e quero usar de novo.** Desarquive e publique novamente.
