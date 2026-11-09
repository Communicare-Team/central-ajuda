---
titulo: Como configurar as mensagens de confirmação e lembrete para o paciente
slug: como-configurar-as-mensagens-de-confirmacao-e-lembrete-para
secao: configuracoes-do-gestor
ordem: 70
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Mensageria
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Envia automaticamente ao paciente um pedido de confirmação da consulta e lembretes antes do horário. Quando o paciente confirma pelo link, o agendamento muda de status sozinho e a recepção só precisa ligar para quem não respondeu.

## Quem pode fazer

Gestores: administrador da conta ou administrador da clínica.

## Onde fica

Depende de a conta usar ou não o **Communicare Conversas**:

- **Sem Communicare Conversas:** **Configurações › Mensageria**
- **Com Communicare Conversas:** **Whatsapp › Disparos** (com os modelos em **Whatsapp › Templates**)

## Antes de começar

- Em **Conta › Clínicas › Editar**, deixe ligado **Enviar e-mails de agendamento para o paciente**. Sem ele, os e-mails não saem.
- Mantenha o e-mail e o celular dos pacientes atualizados.

## Passo a passo: contas sem Communicare Conversas

1. Acesse **Configurações › Mensageria**.
2. Em **Confirmação**, defina quando pedir a confirmação: informe a **Quantidade** e a **Frequência** (dias, horas ou minutos antes do atendimento). Exemplo: 2 dias antes.
3. Configure na coluna **E-mail** (disponível em todos os planos). A coluna **WhatsApp** depende do plano contratado.
4. Em **Lembretes**, defina um ou mais lembretes da mesma forma. Exemplo: 1 dia antes e 4 horas antes.
5. Clique em **Salvar**. A partir daí os envios são automáticos para os novos agendamentos.

## Passo a passo: contas com Communicare Conversas

A confirmação e os lembretes por WhatsApp são feitos com um modelo de mensagem e um gatilho:

1. Crie (ou use) um modelo aprovado pela Meta em **Whatsapp › Templates**, por exemplo, com botões de confirmar e cancelar.
2. Em **Whatsapp › Disparos**, escolha o **Gatilho** (por exemplo, qualquer agendamento), o **Modelo** e quanto tempo antes enviar.
3. Clique em **Adicionar** e depois em **Salvar modificações**.

O passo a passo completo está no tutorial Como configurar um disparo automático de mensagens no WhatsApp, da seção Communicare Conversas. Para criar o modelo, veja Como criar um template de mensagem do WhatsApp.

## Regras importantes

- Quando o paciente confirma pelo link (e-mail ou WhatsApp), o card na agenda passa de amarelo para azul. Na visualização **Lista** da agenda e na sala de espera aparece por onde ele confirmou.
- Os lembretes com teleconsulta levam o link da chamada.
- Cancelar um agendamento cancela os lembretes pendentes dele. Reagendar reprograma os envios para o novo horário.
- Agendamento feito depois do prazo do envio não recebe aquela mensagem. No relatório de envios ele aparece como "Cancelado".
- Encaixes podem não disparar as mensagens. Confira o gatilho escolhido.
- Não exagere na quantidade de envios para não lotar a caixa de entrada do paciente.

## Perguntas frequentes

- **O paciente não recebe o e-mail.** Confira o interruptor de e-mails na clínica e o e-mail no cadastro do paciente.
- **Ninguém está confirmando.** Veja **Whatsapp › Relatório de Envios**. Envios "Cancelados" costumam ser agendamentos feitos em cima da hora, fora do prazo configurado.
- **Como garantir que todo paciente receba alguma mensagem?** Com o Conversas, combine um gatilho que dispara assim que o agendamento é feito com um lembrete algumas horas antes.
- **Dá para enviar a confirmação manualmente?** Sim, pela **Agenda**, na visualização **Lista**.
- **Ao ligar o WhatsApp aparece aviso de plano.** O envio por WhatsApp depende do plano contratado. Fale com o administrador da conta.
