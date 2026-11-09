---
titulo: Como emitir nota fiscal e conferir as emissões
slug: como-emitir-nota-fiscal-e-conferir-as-emissoes
secao: financeiro-e-faturamento
ordem: 120
perfis: Administrador da conta, Administrador da clínica, Recepção
caminho: Financeiro › Asaas › Notas fiscais › Relatórios
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Emite a nota fiscal de serviço do atendimento pela Communicare, sem entrar no site da prefeitura. A nota segue para a prefeitura e, quando aprovada, vai automaticamente para o e-mail do paciente.

## Quem pode fazer

Quem lança recebimentos (gestores e recepção) emite pelo agendamento. A lista de notas fica com os gestores.

## Onde fica

- No agendamento: botão **Gerar nota fiscal** (também no recebimento e nas **Ações rápidas** › **Nota Fiscal**)
- Lista de notas: **Financeiro › Asaas › Notas fiscais › Relatórios**

## Antes de começar

- O cadastro para emissão precisa estar completo e aprovado. Veja Como fazer o cadastro para emissão de nota fiscal.
- O paciente precisa ter nome, CPF, e-mail e endereço. Se faltar algo, o sistema abre a edição do cadastro.

## Passo a passo

**Emitir manualmente**

1. Abra o agendamento (pela Agenda ou Sala de espera) e clique em **Gerar nota fiscal**.
2. Confira o **Emitente** (clínica ou profissional), o paciente e escolha o serviço em **Serviços cadastrados**.
3. Revise o **Valor da nota fiscal** (vem do recebimento; sem recebimento, vem o valor do procedimento), a **Data emissão**, se o **Cliente deve reter ISS?** e escreva **Observações adicionais**, se quiser (por exemplo, dados para reembolso no plano de saúde).
4. Clique em **Emitir**.

**Nota sem agendamento (avulsa)**

1. Em **Financeiro › Asaas › Notas fiscais › Relatórios**, clique em **Adicionar nota fiscal** (ou use **Ações rápidas** › **Nota Fiscal**).
2. Selecione o paciente cadastrado, o serviço, a data e o valor, e clique em **Emitir**.

**Emissão automática**

Com a emissão automática ligada no procedimento, a nota sai sozinha quando o profissional finaliza o atendimento pelo SOAP, desde que:

- o recebimento esteja lançado integralmente antes da finalização (agendamento como **Recebido**);
- o desfecho seja conclusivo (ou a conta não use desfecho);
- o valor recebido seja maior que zero e ainda não exista nota no agendamento.

A nota sai com o valor recebido.

**Conferir as notas**

1. Em **Financeiro › Asaas › Notas fiscais › Relatórios**, filtre por **Data inicial**, **Data final**, **Status** e paciente e clique em **Filtrar**.
2. Em cada nota: **Editar**, **Download** e **Histórico**. Mais detalhes em Como gerar o relatório de notas fiscais.

## Regras importantes

- Caminho da nota: **Agendada** › **Enviada para prefeitura** › **Emitida**. Também pode ficar como **Erro na emissão**, **Processando cancelamento**, **Cancelada** ou **Cancelamento negado**.
- Data de hoje emite na hora; data futura agenda a emissão.
- Só dá para editar nota **Agendada** ou com **Erro na emissão**. O download só libera depois que a nota volta como **Emitida**.
- Recebimento lançado depois da finalização, pagamento parcial ou desfecho inconclusivo não geram nota automática: emita manualmente.

## Perguntas frequentes

- **A nota deu erro. Onde vejo o motivo?** Em **Agenda**, aba **Busca**, localize o paciente e abra o agendamento: o erro aparece ali. Corrija e emita de novo; em instabilidade da prefeitura, edite a nota e reenvie.
- **Dá para emitir nota para empresa (CNPJ) ou paciente estrangeiro sem CPF?** Não pela Communicare. Emita no sistema da prefeitura.
- **Posso cancelar pela Communicare?** Sim, em **Editar** › **Cancelar nota**, mas algumas prefeituras não aceitam cancelamento pela integração.
- **Preciso emitir com valor diferente do recebido.** Na emissão manual, ajuste o valor antes de clicar em **Emitir**.
