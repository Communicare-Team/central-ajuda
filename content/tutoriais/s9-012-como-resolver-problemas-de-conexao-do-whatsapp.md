---
titulo: Como resolver problemas de conexão do WhatsApp
slug: como-resolver-problemas-de-conexao-do-whatsapp
secao: communicare-conversas
ordem: 12
perfis: Administrador da conta, Administrador da clínica
caminho: Conversas › Ajustes › Conta › Canais de atendimento › Detalhes
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Descobrir por que mensagens não saem, não chegam ou ficam paradas, e saber o que fazer quando o número desconecta ou é bloqueado pela Meta.

## Quem pode fazer

Qualquer usuário do Conversas consegue identificar o problema. Reconectar o número e pedir revisão na Meta exige perfil **Administrador** no Conversas e acesso de administrador ao portfólio da clínica na Meta.

## Onde fica

Botão verde **Conversas** no topo do sistema › **Ajustes** › **Conta** › **Canais de atendimento** › **Detalhes** do canal.

## Passo a passo

### 1. Veja a saúde do canal

1. Abra **Canais de atendimento** e clique em **Detalhes** no canal.
2. Confira o indicador de **Integridade**:
   - **Estável:** tudo normal.
   - **Verificando conexão:** possível falha momentânea; nada muda para o atendente.
   - **Em alerta:** aparece aviso na tela e as mensagens enviadas ficam guardadas numa fila protegida.
   - **Crítico:** canal parado. Um administrador precisa verificar bloqueio na Meta ou reconectar.
3. Quando o canal volta a **Estável**, as mensagens guardadas são entregues na ordem certa.

### 2. Reconecte o número

1. Em **Canais de atendimento**, clique em **+** › **WhatsApp CloudAPI** › **Permitir acesso** › **Iniciar**.
2. Clique em **Entrar com Facebook** com o usuário administrador do portfólio.
3. Clique em **Reconectar**, selecione o número, **Continuar** e **Finalizar**.

Quando um canal desconecta, os administradores recebem e-mail com link de reconexão, e a conversa mostra o atalho **Reconectar agora**.

## Regras importantes

- Campanhas pausam sozinhas quando o canal entra em alerta, crítico ou desconecta. Elas só voltam quando um administrador retoma manualmente.
- Se o número for bloqueado (banido): **não** exclua o portfólio, **não** desconecte e **não** tente conectar o número em outro lugar. Isso pode tornar o bloqueio permanente. Veja o motivo no e-mail do portfólio e peça revisão em **Contas do WhatsApp** › **Status da conta** › **Pedir análise**, no Business Manager. A resposta da Meta chega por e-mail.
- A qualidade do número (verde, amarelo, vermelho) fica no Gerenciador do WhatsApp da Meta. Qualidade baixa pode reduzir o limite de envios.

## Erros mais comuns

- **131047:** passaram mais de 24h desde a última mensagem do paciente. Envie um modelo aprovado.
- **131026:** número sem WhatsApp ou digitado errado. Confira +55, DDD e nono dígito.
- **131049 / 131056:** a Meta limitou mensagens de marketing para esse número. Não reenvie na hora; use modelo de utilidade ou aguarde.
- **130497:** país da empresa não preenchido na Meta. Preencha País = Brasil nas informações da empresa.
- **131031:** conta restrita por violação de política. Veja o motivo na Meta e peça revisão.
- **131000:** erro temporário da Meta. Tente de novo; se foi logo após conectar, refaça a conexão.

## Perguntas frequentes

- **As mensagens estão com reloginho e não saem.** Veja a Integridade do canal. Em alerta ou crítico, elas estão guardadas e saem quando a conexão voltar. Se continuar, reconecte.
- **Não consigo responder um paciente que escreveu ontem.** A janela de 24h fechou. Envie um modelo aprovado.
- **Apareceu "Aguardando mensagem" na conversa.** É falha de criptografia: desconecte, atualize o app WhatsApp Business e reconecte. Mensagens perdidas não voltam.
- **Apareceu "Muitas ações em pouco tempo".** É uma pausa de segurança com contador; as ações terminam sozinhas.
- **Nada resolveu.** Use o botão **Falar com o suporte** na Central de Ajuda.
