---
titulo: Como gerar o relatório de notas fiscais
slug: como-gerar-o-relatorio-de-notas-fiscais
secao: relatorios-e-analises
ordem: 10
perfis: Administrador da conta, Administrador da clínica
caminho: Financeiro › Asaas › Notas fiscais › Relatórios
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Reúne em uma única tela todas as notas fiscais emitidas pela clínica, com status, valor e paciente. Assim você confere as emissões, baixa as notas e corrige ou cancela uma nota sem precisar procurar agendamento por agendamento.

## Quem pode fazer

Gestores: administrador da clínica e administrador da conta. O grupo **Financeiro** do menu só aparece para esses perfis.

## Onde fica

**Financeiro › Asaas › Notas fiscais › Relatórios**

## Antes de começar

- A clínica precisa ter o cadastro no Asaas aprovado e a emissão de nota fiscal configurada. Sem isso, a tela de notas não funciona.

## Passo a passo

1. No menu lateral, clique em **Financeiro › Asaas › Notas fiscais › Relatórios**.
2. Preencha os filtros que quiser: **Data inicial**, **Data final**, **Status** e, se for o caso, **Selecionar paciente (opcional)** (busca por nome ou CPF).
3. Clique em **Filtrar**. Se você não preencher nenhum filtro, o sistema mostra todas as notas.
4. Confira a lista: **Paciente**, **Emissão**, **Descrição**, **Status** e **Valor** de cada nota.
5. Use os botões da coluna de ações:
   - **Download**: baixa a nota (aparece só para notas com status Emitida).
   - **Histórico**: mostra o que aconteceu com a nota.
   - **Editar**: abre a nota para corrigir dados, reemitir ou usar **Cancelar nota**.
6. Para emitir uma nota avulsa, sem agendamento, clique em **Adicionar nota fiscal**.

## Regras importantes

- Status possíveis: **Agendada**, **Enviada para prefeitura**, **Emitida**, **Processando cancelamento**, **Cancelada**, **Cancelamento negado** e **Erro na emissão**.
- O botão de download só aparece quando a prefeitura devolve a nota como **Emitida**.
- Notas **Canceladas** ou em **Processando cancelamento** não podem mais ser editadas.
- Notas com **Erro na emissão** podem ser editadas e emitidas de novo. Na maioria dos casos o erro vem de dados faltando no cadastro do paciente (CPF, e-mail ou endereço) ou de instabilidade da prefeitura.
- A nota sai com data de hoje na hora; se você informar uma data futura, ela fica **Agendada**.
- As notas fiscais não aparecem no relatório financeiro. Lá você vê os recebimentos lançados nos agendamentos.
- Cada nota gera automaticamente um lançamento de despesa da tarifa de emissão no financeiro. O valor da tarifa consta no contrato.

## Perguntas frequentes

- **Por que não consigo baixar a nota?** Ela ainda não voltou da prefeitura como Emitida. Aguarde e filtre de novo.
- **Posso cancelar a nota pela Communicare?** Sim, pelo **Editar** › **Cancelar nota**. Algumas prefeituras não aceitam cancelamento pela integração. Nesse caso, o status fica **Cancelamento negado** e o cancelamento precisa ser feito no site da prefeitura.
- **Dá para emitir nota para empresa (CNPJ) ou para paciente estrangeiro sem CPF?** Não. O cadastro do paciente aceita só CPF e endereço nacional. Nesses casos, emita direto no site da prefeitura.
- **Onde vejo o motivo do erro de uma nota?** No menu **Agenda**, aba **Busca**, localize o paciente e edite o agendamento: o erro aparece ali. Se for instabilidade da prefeitura, edite a nota e emita novamente.
