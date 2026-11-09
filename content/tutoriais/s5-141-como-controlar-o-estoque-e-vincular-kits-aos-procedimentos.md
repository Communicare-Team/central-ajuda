---
titulo: Como controlar o estoque e vincular kits aos procedimentos
slug: como-controlar-o-estoque-e-vincular-kits-aos-procedimentos
secao: financeiro-e-faturamento
ordem: 141
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Mat Med
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Controla quanto a clínica tem de cada material e medicamento, avisa quando algo está acabando ou perto de vencer e dá baixa automática nos itens usados nos atendimentos.

## Quem pode fazer

Gestores (administrador da conta ou da clínica).

## Onde fica

**Configurações › Mat Med**, abas **Estoque**, **Fornecedores** e **Movimentações**

## Antes de começar

- Os itens precisam estar no catálogo. Veja Como cadastrar materiais e medicamentos e montar kits (Mat/Med).

## Passo a passo

**1. Ligar o controle no item**

1. Na aba **Catálogo**, edite o item e ligue **Controla estoque**.
2. Em **Configuração de estoque**, informe **Estoque mínimo** (obrigatório), **Estoque máximo**, **Aviso de validade (dias)**, **Categoria de armazenamento** e **Observações de armazenamento**. Salve.

**2. Cadastrar fornecedores**

1. Na aba **Fornecedores**, clique em **Novo Fornecedor**.
2. Informe o **CNPJ** (os dados da empresa são preenchidos automaticamente) ou preencha à mão, com contato e endereço. Também dá para cadastrar durante uma entrada.

**3. Registrar entradas e saídas**

1. Na aba **Movimentações**, clique em **Nova movimentação**.
2. Escolha o tipo:
   - **Compra**: entrada com nota fiscal (clínica, fornecedor, data de entrada, número, data e valor da nota e itens);
   - **Manual**: entrada avulsa sem nota;
   - **Perda** (quebra, dano ou extravio), **Vencimento** (item vencido descartado), **Inventário** (acerto por contagem) ou **Transferência** (saída para outra clínica).
3. Informe itens, quantidades e lote, e salve.

**4. Vincular kits e itens aos procedimentos**

1. Em **Configurações › Procedimentos**, edite um procedimento do tipo exame/procedimento.
2. Na modalidade de pagamento, abra **Itens de terapia** e adicione itens do catálogo ou um kit inteiro. Ajuste as quantidades e remova o que não for usado.
3. Confira os profissionais executores e salve. Sem executor, o procedimento não aparece na agenda do profissional.

## Regras importantes

- Ao finalizar o atendimento, os itens de terapia usados recebem baixa automática no estoque.
- Os itens também podem ser ajustados no agendamento (procedimentos associados, editar itens de terapia) e pelo profissional durante o atendimento, no Objetivo, em procedimentos.
- A aba **Estoque** mostra o saldo de cada item com status **OK**, **Crítico** (abaixo do mínimo), **Vencendo** e **Zerado**. Clique nos cartões para filtrar.
- O controle é por clínica: entradas e saídas registram a clínica de origem.

## Perguntas frequentes

- **Onde vejo o que está acabando?** Na aba **Estoque**, clique no cartão **Crítico**. Para validade, use **Vencendo**.
- **O kit não aparece ao agendar.** Confira se o procedimento tem profissionais executores e se o kit está ativo.
- **Contei o estoque e o saldo está diferente.** Registre uma movimentação do tipo **Inventário** com a quantidade correta.
