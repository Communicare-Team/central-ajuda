---
titulo: Como gerar o relatório financeiro
slug: como-gerar-o-relatorio-financeiro
secao: relatorios-e-analises
ordem: 20
perfis: Administrador da conta, Administrador da clínica
caminho: Relatórios › Financeiro
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Mostra, atendimento por atendimento, quanto foi cobrado, quanto já entrou, quanto falta receber e quanto vai de repasse para cada profissional. É a base para fechar o mês, pagar repasses e projetar o caixa a partir da agenda.

## Quem pode fazer

Gestores (administrador da clínica e administrador da conta) e demais usuários que não estejam marcados como restritos. Usuário restrito vê o aviso de que não tem permissão para relatórios financeiros.

## Onde fica

**Relatórios › Financeiro**, aba **Financeiro**

## Antes de começar

- Os valores só aparecem se o recebimento tiver sido lançado no agendamento. Agendamento sem recebimento entra como **A receber**.
- Para ver repasse, o repasse precisa estar configurado no procedimento.

## Passo a passo

1. No menu lateral, clique em **Relatórios › Financeiro** e fique na aba **Financeiro**.
2. Escolha os filtros:
   - **Clínicas**, **Modalidade de pagamento** (Particular ou convênios), **Forma de recebimento**, **Profissionais**, **Procedimentos** e **Time**.
   - **Desde** e **Até**: período da data do agendamento (obrigatório).
   - **Recebimento desde** e **Recebimento até** (opcional): limita aos recebimentos feitos nessas datas.
   - **Pagamento**: **A receber**, **Recebido (a compensar)**, **Recebido (compensado)** ou **Estornado**.
3. Clique em **Gerar relatório**.
4. Confira as colunas: agendamento, paciente, profissional, procedimento, desfecho, modalidade, valor do procedimento, desconto, voucher, recebido, impostos, taxas, parcela, repasse, status do repasse, datas de recebimento e de compensação e a parte da clínica (provisionada e efetivada).
5. Para levar os dados para o Excel, dê um nome em **Nome do arquivo** e clique em **Exportar planilha**.

## Regras importantes

- Clínica e período são obrigatórios. Sem eles, aparece "Por favor, preencha todos os campos obrigatórios" ou "Por favor, selecione o período de datas".
- O período principal considera a **data do agendamento**, não a do pagamento. Para ver o que entrou em um mês, use um período de agendamento amplo e preencha **Recebimento desde/até** com o mês desejado.
- Recebimento parcelado aparece uma linha por parcela.
- Consulta com procedimento associado aparece com um "+" na coluna de procedimento; na planilha, consulta e procedimento saem em linhas separadas.
- Notas fiscais não entram neste relatório.
- Ao filtrar períodos antigos, prefira **Todos** em Procedimentos. **Todos ativos** deixa de fora agendamentos de procedimentos que foram inativados depois.

## Sobre o relatório "Financeiro (legado)"

O relatório antigo, na aba **Financeiro (legado)**, está saindo do menu. Use a aba **Financeiro** para as conferências do dia a dia. Os vídeos e materiais antigos que mostram a aba legado estão desatualizados.

## Perguntas frequentes

- **O valor da receita do dia não bate com o extrato.** Confira o filtro **Pagamento**: valores a compensar ainda não estão no extrato. Compare com **Financeiro › Receitas e despesas**.
- **O valor base duplica nas parcelas?** Não. Ele se repete em cada parcela só como referência. Para a contabilidade, use as colunas de recebido, repasse e clínica.
- **Por que um atendimento não aparece?** Provavelmente o recebimento não foi lançado no agendamento, ou o período escolhido não inclui a data do agendamento.
- **Como gero o relatório de um só profissional?** Selecione apenas ele em **Profissionais** e exporte a planilha para enviar a ele.
- **Quantas vezes um paciente fez um procedimento?** Exporte o relatório do período e filtre na planilha.
