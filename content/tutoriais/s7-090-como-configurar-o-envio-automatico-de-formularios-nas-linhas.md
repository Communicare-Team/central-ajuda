---
titulo: Como configurar o envio automático de formulários nas linhas de cuidado
slug: como-configurar-o-envio-automatico-de-formularios-nas-linhas
secao: funcionalidades-avancadas
ordem: 90
perfis: Administrador da clínica, Administrador da conta
caminho: Gestão de cuidados › Programas
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Envia formulários (escalas, questionários de acompanhamento, pré-consulta) pelo WhatsApp de forma automática, no ritmo definido pela linha de cuidado, sem a equipe precisar lembrar de mandar o link a cada paciente.

## Quem pode fazer

Gestores (administrador da clínica ou da conta) e usuários habilitados como cuidadores que editam programas.

## Onde fica

- **Gestão de cuidados › Programas** (cuidado do tipo formulário)
- **Whatsapp › Templates** e **Whatsapp › Disparos** (mensagem e gatilho)

## Antes de começar

- O formulário precisa existir em **Configurações › Formulários personalizados**, com **Coletar CPF no formulário?** ligado. Veja Como criar instrumentos e questionários (formulários personalizados).
- O envio automático exige o **Communicare Conversas** com WhatsApp conectado.
- O paciente precisa ter CPF e celular no cadastro.

## Passo a passo

1. Em **Gestão de cuidados › Programas**, abra a linha de cuidado em **Editar** (ou crie em **Adicionar**).
2. No grupo de pacientes, adicione um cuidado do tipo **Preenchimento de formulário**.
3. Em **Formulário**, escolha o formulário. Em **Início Após (opcional)**, informe em quantos dias após a entrada na linha ele deve ser enviado.
4. Defina a repetição: **A cada** (ex.: 90 dias) e **Qtd repetições** ou **Ilimitado**. Salve o programa.
5. Em **Whatsapp › Templates**, crie a mensagem (ex.: "Olá, [primeiro nome], responda o questionário para a continuidade do seu acompanhamento") e insira o dado dinâmico **link do formulário**. Siga Como criar um template de mensagem do WhatsApp: o template precisa ser aprovado e sincronizado antes do uso.
6. Em **Whatsapp › Disparos**, crie um disparo com o gatilho **Cuidado de formulário a vencer**: escolha a **Hora do dia**, quanto tempo antes do vencimento enviar e o template. Detalhes em Como configurar um disparo automático de mensagens no WhatsApp.
7. Se quiser cobrar quem não respondeu, crie outro disparo com o gatilho **Cuidado de formulário vencido**.

## Enviar um formulário antes de toda consulta

Para pré-consulta, sem linha de cuidado: crie um template com o link do formulário e um disparo com gatilho de agendamento (ex.: qualquer agendamento realizado, 24 horas antes do horário do atendimento). Também é possível exigir o formulário no agendamento online.

## Regras importantes

- O cuidado de formulário é concluído automaticamente quando o paciente termina de responder.
- Gatilhos de cuidado exigem um horário fixo do dia.
- **Dias para responder novamente** no formulário limita reenvios ao mesmo paciente.
- Alterar o cuidado no grupo vale para os pacientes já incluídos.
- Em disparos "antes", se o horário calculado já passou há mais de 1 hora, a mensagem é cancelada.
- O mesmo funciona para cuidados individuais do tipo formulário.

## Perguntas frequentes

- **O paciente recebeu o link, mas a resposta não aparece no prontuário.** Se **Validar pelo profissional?** estiver ligado, o profissional precisa abrir a aba do formulário e salvar.
- **A mensagem não foi enviada.** Confira se o template é da conexão atual do WhatsApp e se está aprovado.
- **Posso usar uma mensagem para todos os formulários?** Sim, o dado dinâmico coloca o link certo de cada cuidado.
