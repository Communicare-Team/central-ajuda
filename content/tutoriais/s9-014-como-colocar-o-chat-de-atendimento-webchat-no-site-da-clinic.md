---
titulo: Como colocar o chat de atendimento (WebChat) no site da clínica
slug: como-colocar-o-chat-de-atendimento-webchat-no-site-da
secao: communicare-conversas
ordem: 14
perfis: Administrador da conta
caminho: Conversas › Ajustes › Canais de atendimento › Novo canal › WebChat
video: 
video_rotulo: 
atualizado: 2026-11-05
---
## Para que serve

Oferecer aos visitantes do site da clínica um canal de conversa direto com a recepção. Há duas opções: o **WebChat**, um chat próprio acessado por link ou QR Code, que não depende da Meta; e o **Widget de Atendimento**, um botão instalado no site que leva o visitante para o WhatsApp, o WebChat, o Instagram ou o Messenger.

## Quem pode fazer

Usuário com perfil **Administrador** no Conversas. Para instalar o widget, é preciso também ter acesso ao código do site (ou à pessoa que cuida dele).

## Onde fica

- WebChat: botão verde **Conversas** no topo do sistema › **Ajustes** › **Canais de atendimento** › **Novo canal** › **WebChat**.
- Widget: **Ajustes** › **Integrações** › **Widget de Atendimento** › **Configurar**.

## Antes de começar

- Configure o horário de atendimento: o WebChat mostra **Online** ou **Offline** de acordo com ele.

## Passo a passo

### Criar o WebChat

1. Em **Canais de atendimento**, clique em **Novo canal** › **WebChat**.
2. Preencha o **Nome do canal** (o visitante vê esse nome) e, se quiser, troque o ícone em **Alterar**.
3. Deixe ligado o **Indicador de digitando**, se quiser que o paciente veja quando alguém está escrevendo.
4. Clique em **Salvar alterações**. O sistema gera um link curto (**Copiar**) e um QR Code (**Baixar QR Code**) para divulgar.

### Criar e instalar o widget no site

1. Em **Widget de Atendimento**, clique em **+ Novo** e escolha **Versão atual**.
2. Defina o comportamento: mostrar uma lista de assuntos (cada um levando a um canal) ou abrir direto o WhatsApp ou o WebChat com um texto pronto.
3. Monte o formulário: **Nome** e **WhatsApp** são obrigatórios; e-mail, Instagram e campos personalizados são opcionais. Se quiser, ligue **Exigir consentimento** e **Rastreamento do cliente** (mostra a origem e as páginas visitadas no atendimento).
4. Ajuste a aparência: nome da clínica, mensagem de abertura, cores, imagem e ícone do botão.
5. Copie o script e peça para colar dentro da área de cabeçalho (head) do site.
6. Preencha **Domínios de instalação** com o endereço do site e salve. O widget leva de 1 a 2 minutos para aparecer.

## Regras importantes

- Sem domínio preenchido em **Domínios de instalação**, o widget não funciona em lugar nenhum.
- **Testar widget** cria um atendimento real na caixa de entrada.
- O visitante preenche nome e WhatsApp e aceita o termo de consentimento antes de conversar. Se voltar por outro aparelho, recebe um código de 6 dígitos pelo WhatsApp.
- No WebChat o visitante pode enviar texto, áudio e até 10 arquivos por vez (até 50 MB cada).
- Remover o WebChat é irreversível: os atendimentos abertos são concluídos e o link e o QR Code param na hora.
- O WebChat no site da clínica está disponível no plano do Communicare Conversas. Em caso de dúvida sobre os canais do seu plano, fale com o suporte.
- O número de canais WebChat por conta é limitado; se aparecer aviso de limite, fale com a Communicare.

## Perguntas frequentes

- **Instalei o script e o botão não aparece.** Confira se o domínio do site está em **Domínios de instalação**, aguarde 1 a 2 minutos e veja se não ficaram dois scripts no site (o antigo e o novo).
- **Tenho um botão de WhatsApp antigo no site.** Widgets antigos aparecem marcados como versão anterior. Crie uma cópia na versão atual e remova o script antigo do site.
- **Dá para mudar a cor do WebChat aberto pelo link?** Não. Para personalizar a aparência, use o widget.
- **O WebChat tem custo por mensagem?** Não. O WebChat está disponível no plano do Communicare Conversas e não usa a Meta, então não há cobrança da Meta por mensagem. Em caso de dúvida sobre os canais do seu plano, fale com o suporte.
