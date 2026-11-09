---
titulo: Como cadastrar categorias e centros de custo
slug: como-cadastrar-categorias-e-centros-de-custo
secao: financeiro-e-faturamento
ordem: 30
perfis: Administrador da conta
caminho: Financeiro › Receitas e despesas › Categorias
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

As categorias funcionam como o plano de contas da clínica: dizem de onde vem cada receita (consulta, procedimento) e para onde vai cada despesa (aluguel, contador, energia). Os centros de custo separam os lançamentos por área ou unidade (por exemplo, pediatria e psicologia). Com os dois bem cadastrados, o extrato e o fluxo de caixa mostram totais organizados.

## Quem pode fazer

Dono da conta e Admin de Conta.

## Onde fica

- **Financeiro › Receitas e despesas › Categorias**
- **Financeiro › Receitas e despesas › Centros de custo**

## Antes de começar

- Peça ao contador o plano de contas de receitas e despesas usado no DRE da clínica. Cadastrar categorias parecidas facilita a conversa com a contabilidade.

## Passo a passo

### Categorias

1. Acesse **Financeiro › Receitas e despesas › Categorias**.
2. Clique em **Adicionar categoria**.
3. Escolha o **Tipo** (receita ou despesa) e escreva a **Descrição**.
4. Para criar um grupo (por exemplo, "Despesas fixas"), deixe **Subcategoria de** em branco e clique em **Salvar**.
5. Para criar um item dentro do grupo (por exemplo, "Aluguel"), clique de novo em **Adicionar categoria**, preencha a descrição e selecione o grupo em **Subcategoria de**. Clique em **Salvar**.

### Centros de custo

1. Acesse **Financeiro › Receitas e despesas › Centros de custo**.
2. Clique em **Adicionar centro de custo**.
3. Preencha **Nome** e **Descrição** e clique em **Salvar**.

## Regras importantes

- Já vêm categorias padrão do sistema (como Consulta, na receita, e a tarifa de cobrança, na despesa). Elas não podem ser editadas nem excluídas.
- O tipo da categoria não muda depois de criada. Se errou, crie outra.
- Uma categoria com subcategorias não pode ser excluída. Se ela já tem lançamentos, o sistema pede uma **Nova categoria** para transferi-los antes de excluir.
- As categorias de receita são escolhidas no cadastro dos procedimentos; assim, cada recebimento cai na categoria certa automaticamente. As de despesa são usadas nos lançamentos de contas a pagar e nas taxas das formas de recebimento.
- Centro de custo é opcional. Ele não é excluído: use **Inativar** e, se precisar, **Reativar**. O campo só aparece nos lançamentos quando há pelo menos um centro ativo.
- Nome do centro de custo: até 64 caracteres; descrição: até 256.
- Com integração Omie ativa, o botão **Atualizar com Omie** traz as categorias e os departamentos (que viram centros de custo).

## Perguntas frequentes

- **Só aparece "Consulta" nas categorias de receita do procedimento.** Crie uma categoria de receita "Procedimento" em **Adicionar categoria** e selecione-a no cadastro do procedimento.
- **Preciso usar centro de custo?** Não. Ele é útil para clínicas com várias áreas ou unidades que querem separar despesas.
- **Como vejo as despesas por categoria?** No **Fluxo de caixa**, que totaliza receitas e despesas por categoria, ou no **Extrato**, filtrando o tipo Despesa.
