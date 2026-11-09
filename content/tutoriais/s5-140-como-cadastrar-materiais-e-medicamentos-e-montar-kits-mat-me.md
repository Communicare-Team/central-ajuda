---
titulo: Como cadastrar materiais e medicamentos e montar kits (Mat/Med)
slug: como-cadastrar-materiais-e-medicamentos-e-montar-kits-mat
secao: financeiro-e-faturamento
ordem: 140
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Mat Med
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

O Mat/Med é o catálogo de materiais, medicamentos e taxas da clínica. Com os itens cadastrados (e agrupados em kits), eles entram nos procedimentos e nas guias SADT com o código e o preço certos, sem digitar tudo de novo a cada atendimento.

## Quem pode fazer

Gestores (administrador da conta ou da clínica).

## Onde fica

**Configurações › Mat Med**, abas **Catálogo** e **Kits**

## Passo a passo

**Cadastrar um item no catálogo**

1. Acesse **Configurações › Mat Med** e abra a aba **Catálogo**.
2. Clique em **Adicionar item**.
3. Preencha **Nome**, **Tipo** (material, medicamento, OPME, taxas e aluguéis, gases medicinais), **Unidade de medida** e **Unidade TISS**. Para OPME, informe também **Registro ANVISA**, **Fabricante** e **Código ref. fabricante**.
4. Se o item terá controle de estoque, ligue **Controla estoque** e preencha a configuração. Veja Como controlar o estoque e vincular kits aos procedimentos.
5. Salve.

**Cadastrar os preços**

1. Edite o item e adicione um preço para cada convênio (ou particular): **Convênio**, **Tabela**, **Código**, **Valor** e, se houver, **Fator Red/Acrésc**.
2. Marque **Necessita autorização prévia do convênio** quando a operadora exigir guia autorizada para o item.

**Importar vários itens de uma vez**

1. Na aba **Catálogo**, clique em **Baixar template Excel**, preencha a planilha e use **Importar planilha**.
2. O histórico mostra cada importação e os itens com problema.

**Montar um kit**

1. Abra a aba **Kits** e clique em **Novo Kit**.
2. Dê um nome, uma descrição (opcional) e use **Buscar item no catálogo** para incluir os itens e as quantidades. Exemplo: kit de curativo com gaze, soro e luva.
3. Salve.

## Regras importantes

- O tipo do item segue a classificação usada nas guias TISS: materiais, medicamentos, taxas e OPME saem em campos separados da guia SADT.
- Os preços valem por convênio: o mesmo item pode ter valor diferente em cada operadora.
- Kits e itens podem ser editados ou desativados; itens inativos ficam fora das buscas.
- Use **Exportar Excel** para tirar uma cópia do catálogo.

## Perguntas frequentes

- **Como uso o kit no atendimento?** Vincule o kit aos **Itens de terapia** do procedimento. Veja Como controlar o estoque e vincular kits aos procedimentos.
- **Os itens antigos digitados à mão nos procedimentos continuam valendo?** Desde abril de 2026 os itens de terapia são buscados no catálogo. Revise os procedimentos antigos e troque pelos itens do catálogo para manter códigos e preços corretos.
- **Preciso controlar estoque para usar o catálogo?** Não. O controle de estoque é opcional por item.
