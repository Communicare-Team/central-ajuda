---
titulo: Como consultar estornos de pagamentos
slug: como-consultar-estornos-de-pagamentos
secao: financeiro-e-faturamento
ordem: 67
perfis: Administrador da conta
caminho: Financeiro › Asaas › Estornos
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Quando um pagamento online é devolvido ao paciente (por cancelamento da consulta ou por estorno feito pela clínica), o processo passa pelo banco e pode levar alguns dias. A tela de estornos reúne todos esses pedidos em um só lugar para a clínica acompanhar o andamento, entender falhas e enviar o comprovante ao paciente.

## Quem pode fazer

Admin de Conta (o pedido de estorno e o histórico têm acesso restrito).

## Onde fica

**Financeiro › Asaas › Estornos** (tela **Histórico de estornos**)

## Antes de começar

- A tela mostra estornos de pagamentos feitos online (link de pagamento, Agenda Online ou fila de atendimento), pela conta de pagamento online da clínica.
- Pagamentos recebidos na clínica (dinheiro, maquininha, Pix direto) não passam por aqui. Para esses, desfaça o recebimento no agendamento e faça a devolução por fora.

## Passo a passo

1. Acesse **Financeiro › Asaas › Estornos**.
2. A lista mostra os estornos do mais recente para o mais antigo, com **Paciente**, **Atendimento**, **Tipo** (agendamento ou fila de atendimento), **Forma** (cartão ou Pix), **Valor pago**, **Valor estornado**, **Solicitado em**, **Confirmado em** e **Status**.
3. Para encontrar um paciente, digite o nome ou o CPF em **Buscar por nome ou CPF** e clique em **Buscar**. Use **Limpar filtros** para voltar à lista completa.
4. Para ver todos os passos de um estorno, clique em **Ver histórico do estorno**. O histórico mostra a origem do pagamento, a confirmação, o pedido de estorno, eventuais erros e a conclusão. Use **Filtrar histórico** para ver **Todos**, só **Estorno** ou só **Pagamento**.
5. Dentro do histórico, **Ver outros pagamentos do paciente** lista os demais pagamentos dele e seus status.
6. Para enviar o comprovante ao paciente, clique em **Abrir comprovante** e baixe o PDF.

## O que significa cada status

- **Solicitado**: o pedido foi enviado e está em andamento.
- **Confirmado**: o valor foi devolvido.
- **Parcial**: só parte do valor foi estornada.
- **Falhou** ou **Negado**: o estorno não foi concluído. O motivo aparece no histórico.
- **Aprovado sem confirmação**: o pedido foi aceito, mas a confirmação final ainda não chegou.

## Regras importantes

- Em cartão de crédito, o valor costuma aparecer na fatura do paciente em 7 a 15 dias úteis. Em Pix, em até 2 dias úteis.
- Consultas pagas online e canceladas podem gerar estorno automático, conforme as regras da conta.
- Na agenda, o Admin de Conta encontra os botões **Estornar pagamento** e **Estornar e cancelar** no agendamento. O segundo devolve o valor e também cancela a consulta.
- Quando o comprovante ainda não existe, o botão aparece desabilitado com o aviso "Sem comprovante disponível".

## Perguntas frequentes

- **O paciente diz que não recebeu o estorno.** Confira o status. Se estiver **Confirmado**, envie o comprovante e lembre o prazo do cartão. Se estiver **Falhou**, veja o motivo no histórico e fale com o suporte.
- **Não vejo o botão de estornar no agendamento.** Ele aparece só para Admin de Conta e só para pagamentos feitos online.
