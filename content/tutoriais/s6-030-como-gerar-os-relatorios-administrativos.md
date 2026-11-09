---
titulo: Como gerar os relatórios administrativos
slug: como-gerar-os-relatorios-administrativos
secao: relatorios-e-analises
ordem: 30
perfis: Administrador da conta, Administrador da clínica, Recepção, Profissional de saúde
caminho: Relatórios › Administrativo
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Mostra o que aconteceu com os agendamentos e atendimentos da clínica em um período: quantos foram agendados, confirmados, cancelados, atendidos e faltas. Serve para acompanhar a produção, conferir a agenda e levantar o histórico de um paciente.

## Quem pode fazer

Gestores e demais usuários que não estejam marcados como restritos. O profissional pode filtrar apenas os próprios atendimentos, e cada usuário só vê as clínicas a que tem acesso.

## Onde fica

**Relatórios › Administrativo**, com duas abas: **Agendamentos e atendimentos** (detalhado) e **Geral** (resumo em números).

## Passo a passo

### Relatório detalhado (Agendamentos e atendimentos)

1. Clique em **Relatórios › Administrativo** e abra a aba **Agendamentos e atendimentos**.
2. Escolha os filtros: **Clínicas**, **Profissionais**, **Modalidade de pagamento**, **Procedimentos**, **Tipo de agendamento**, **Status atendimento / Finalização**, **Encaixe**, **Teleconsulta**, **Time**, **Pacientes ativos** e, se quiser, **Buscar paciente (Nome ou CPF)**.
3. Em **Preset**, escolha o conjunto de colunas: **Dados Cadastrais**, **Dados de Atendimento**, **Dados Financeiros** ou **Todos os Campos**. Ajuste coluna por coluna em **Campos**, se precisar.
4. Informe o período em **Desde** e **Até**.
5. Clique em **Gerar relatório**. Com muitos dados, pode demorar um pouco.
6. Para baixar, dê um nome em **Nome do arquivo** e clique em **Exportar planilha**.

### Relatório geral

1. Abra a aba **Geral**.
2. Escolha **Clínicas**, **Profissionais**, **Procedimentos**, **Time** e o período.
3. Clique em **Gerar relatório** para ver os totais: agendamentos, confirmados, cancelados, atendimentos, tempo médio de consulta e pontualidade, entre outros.

## Regras importantes

- O período considera a **data do agendamento**.
- Os filtros já vêm com **Todos** selecionado. Uma boa prática é deixar tudo em Todos e tirar as colunas que não precisa na planilha.
- **Tipo de agendamento**: **Reagendado** é o agendamento original que foi remarcado; **Reagendamento** é o novo agendamento criado a partir dele; **Encaixe** é atendimento feito pelo botão de encaixe.
- **Finalizado automaticamente**: o atendimento foi iniciado e não foi finalizado; o sistema finaliza sozinho após 12 horas.
- **Conclusivo** e **inconclusivo** vêm dos desfechos configurados pela clínica. Sem desfechos configurados, o atendimento finalizado aparece como conclusivo.
- Colunas com "(legado)" mostram o formato antigo de status e desfecho. Use as colunas sem "(legado)".
- O relatório não traz o conteúdo das evoluções do prontuário.
- Em volumes grandes, a planilha é dividida em abas.

## Perguntas frequentes

- **Como vejo só quem foi atendido?** Em **Status atendimento / Finalização**, marque os status finalizados (incluindo **Finalizado automaticamente**).
- **Existe filtro de presença?** Não. Use a coluna **Chegada**, que mostra o horário em que a presença foi marcada.
- **Como vejo tudo o que um paciente fez na clínica?** Busque o paciente pelo nome ou CPF e use um período amplo.
- **O relatório mostra atendimentos que não vejo na agenda.** Confira os status: cancelados, reagendados e encaixes também entram no relatório.
