---
titulo: Como criar os procedimentos de consultas e exames
slug: como-criar-os-procedimentos-de-consultas-e-exames
secao: configuracoes-para-profissionais
ordem: 30
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Procedimentos
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Cadastrar as consultas, exames e procedimentos que a clínica realiza, com duração, valor, repasse e quem atende. Agendamento, prontuário, financeiro e relatórios dependem desse cadastro.

## Quem pode fazer

Gestor da clínica (administrador da clínica ou da conta). O profissional só consulta os procedimentos dele em **Personalização › Meus procedimentos**, sem editar.

## Onde fica

**Configurações › Procedimentos**

## Antes de começar

- Para usar convênio, cadastre antes o convênio em **Configurações › Convênios**.
- Pesquise se o procedimento já existe (**Buscar**, inclusive na aba **Inativos**). O sistema não aceita dois procedimentos com o mesmo nome.

## Passo a passo

1. Clique em **Adicionar**.
2. Em **Tipo de procedimento**, escolha **Consulta** ou **Exame / Procedimento**.
3. Selecione as **Clínicas** onde ele será usado.
4. Para exame/procedimento, ligue **Agendável** se ele puder ser marcado direto na agenda.
5. Escolha a **Categoria da receita** e, se usar, o **Centro de custo**.
6. Informe a **Duração** em minutos. É o tempo que fica ocupado na agenda.
7. Preencha **Nome para uso interno** (equipe, agenda e relatórios) e **Nome para agenda online** (o que o paciente vê nos recibos e na Agenda Online).
8. Em modalidades de pagamento, adicione uma linha por forma de cobrança:
   - **Particular**: **Valor do procedimento**.
   - **Convênio**: escolha **Convênio**, **Plano** e o **Procedimento (TUSS)**.
   - **Crédito**: quantidade de créditos, para pacotes.
9. Em cada modalidade, defina o repasse: **Tipo repasse profissional** (**Fixo** ou **Porcentagem**) e **Valor do profissional**. Se ajustar, configure os abatimentos (**Impostos**, **Custo por transação**, **Desconto para pacientes**) e as **Exceções** por profissional.
10. Em **Profissionais executores**, use **Quem pode executar** para escolher todos, profissionais específicos ou uma especialidade.
11. Se quiser, vincule **Exames / Procedimentos associados**.
12. Salve. Na lista, ligue conforme o uso **Agenda online**, **Teleconsulta** e **Pagamento Online**.

## Regras importantes

- Procedimento sem o profissional como executor não aparece na agenda dele.
- **Consulta** gera guia de consulta TISS; **Exame / Procedimento** gera guia SP/SADT. O código TUSS só é necessário para convênio.
- Exame/procedimento não agendável é registrado dentro de um atendimento ou associado a uma consulta. Associados entram juntos no agendamento e somam no valor.
- **Teleconsulta** só liga se todos os executores tiverem teleconsulta contratada.
- **Pagamento Online** só aparece com a conta de pagamentos (Asaas) ativa. Ligado, o paciente paga antes de concluir o agendamento online.
- Retorno com a mesma duração da consulta pode ser outra modalidade (valor zero). Com duração diferente, crie outro procedimento.
- Profissional inativado sai automaticamente dos procedimentos.
- Use **Duplicar** para criar variações e **Desativar** em vez de apagar.

## Perguntas frequentes

- **Aparece "Já existe um procedimento com este nome", mas não acho nenhum.** Procure na aba **Inativos**; nomes valem para todas as clínicas da conta.
- **Como usar o mesmo procedimento em outra clínica?** Edite-o e marque as duas em **Clínicas**.
- **Ativei a teleconsulta e o procedimento não virou online.** Ligue também **Teleconsulta** na lista de procedimentos.
- **O procedimento não aparece na Agenda Online.** Confira **Agenda online** ligado, o profissional como executor e os horários dele com Agenda Online ativa.
- **Posso cobrar um receituário ou medicamento?** Sim, cadastre como procedimento com valor.
