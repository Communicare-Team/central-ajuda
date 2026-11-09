---
titulo: Como cadastrar as formas de recebimento
slug: como-cadastrar-as-formas-de-recebimento
secao: financeiro-e-faturamento
ordem: 20
perfis: Administrador da conta
caminho: Financeiro › Receitas e despesas › Formas de recebimento
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

As formas de recebimento dizem ao sistema como o paciente pagou (Pix, dinheiro, débito, crédito) e o que acontece com esse dinheiro: quanto a operadora desconta, em quantos dias cai e em qual conta entra. Com isso, cada recebimento lançado aparece no extrato já pelo valor líquido e na data certa.

## Quem pode fazer

Dono da conta e Admin de Conta.

## Onde fica

**Financeiro › Receitas e despesas › Formas de recebimento**

Atenção: existe outro item com o mesmo nome em **Financeiro › Asaas › Cobranças › Formas de recebimento**. Esse segundo é só para o pagamento online (link de pagamento e Agenda Online), com parcelamento e taxas do banco já preenchidas. Este tutorial trata das formas usadas no recebimento feito na clínica.

## Antes de começar

- Cadastre as **contas**, as **categorias** (inclusive uma de despesa para as taxas) e, se usar, os **centros de custo**.

## Passo a passo

1. Acesse **Financeiro › Receitas e despesas › Formas de recebimento**.
2. Clique em **Adicionar recebimento**.
3. Preencha:
   - **Forma de pagamento**: um nome claro, por exemplo "Pix Banco X" ou "Crédito maquininha".
   - **Operadora do pagamento (taxas)**: a maquininha ou operadora, se houver. Para Pix e dinheiro pode ficar em branco.
   - **Taxa por transação**: percentual cobrado pela operadora.
   - **Custo por transação**: valor fixo cobrado por operação, se existir.
   - **Prazo de recebimento**: em dias (0 = cai no mesmo dia).
   - **Centro de custo das taxas** e **Categoria das taxas**: onde a despesa com a taxa será registrada.
   - **Conta de recebimento**: a conta onde o valor vai entrar.
4. Clique em **Salvar**.

## Regras importantes

- Já vêm formas cadastradas (Dinheiro, Crédito, Débito, Pix). Você pode editar, inativar ou criar novas, mas o nome não pode repetir exatamente esses tipos padrão.
- Ao lançar um recebimento com essa forma, o sistema registra a entrada na data do prazo e lança a taxa como despesa. No extrato, esse lançamento aparece como **Múltipla** (receita + taxa).
- Sem taxa nem custo, preencha 0. Assim o valor entra cheio.
- Quanto mais detalhado o cadastro (crédito à vista, crédito parcelado, débito), mais fiel fica o saldo.
- Formas inativas vão para a aba **Inativos**. O ícone de **Histórico** mostra o que foi alterado, com valor antigo e novo.

## Perguntas frequentes

- **Qual das duas telas de formas de recebimento devo usar?** **Receitas e despesas** para o que o paciente paga na clínica; **Asaas › Cobranças** para o pagamento online.
- **A forma que o paciente usou não aparece na hora de lançar.** Verifique se ela está na aba **Ativos**. Formas do tipo convênio só aparecem em agendamentos de convênio.
- **Onde vejo as taxas descontadas?** No extrato, no lançamento múltiplo do recebimento.
- **Quais são as taxas do pagamento online?** Elas aparecem na tela **Asaas › Cobranças › Formas de recebimento** e seguem o contrato.
