---
titulo: Como fazer o cadastro para emissão de nota fiscal
slug: como-fazer-o-cadastro-para-emissao-de-nota-fiscal
secao: financeiro-e-faturamento
ordem: 110
perfis: Administrador da conta, Administrador da clínica, Profissional de saúde
caminho: Financeiro › Asaas › Dados cadastrais
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Deixa a conta pronta para emitir nota fiscal de serviço (NFS-e) pela Communicare, de forma manual ou automática ao finalizar o atendimento. A emissão é feita pelo Asaas, por isso é preciso ter conta Asaas mesmo sem usar o pagamento online.

## Quem pode fazer

O gestor configura a parte da clínica. Se a nota for emitida em nome do profissional, ele faz a parte dele no próprio login. Recomendamos fazer junto com o contador.

## Onde fica

- Clínica: **Financeiro › Asaas › Dados cadastrais** e **Financeiro › Asaas › Notas fiscais › Serviços**
- Profissional: **Personalização › Minha conta Asaas › Dados cadastrais** e **Personalização › Minha conta Asaas › Notas fiscais › Serviços**

## Antes de começar

- Defina quem emite as notas: a clínica (CNPJ da clínica) ou cada profissional (CNPJ do profissional). Conta de pessoa física não emite nota.
- Tenha com o contador: código do serviço municipal, alíquota de ISS, retenções e, se a empresa não for do Simples Nacional, a situação tributária de PIS/COFINS.

## Passo a passo

São cinco requisitos, nesta ordem.

**1. Conta Asaas da clínica aprovada**

1. Em **Financeiro › Asaas › Dados cadastrais**, preencha os dados da empresa, as **Taxas** (retenções) e, se quiser, as **Observações adicionais** que saem em todas as notas.
2. Empresa fora do Simples: clique em **Editar**, preencha a seção **PIS/COFINS (NT-007)** e salve. Sem isso a emissão fica bloqueada.
3. Conclua a abertura no painel do Asaas (senha, celular e documentos). No painel do Asaas, em **Notas fiscais › Configurações**, informe inscrição municipal e acesso da prefeitura (algumas exigem certificado digital).
4. Aguarde **Status informações comerciais** e **Status documentação** como **Aprovado**.

**2. Escolher o emitente**

1. Ainda em **Financeiro › Asaas › Dados cadastrais**, em **Emitente da nota automática**, escolha **Clínica** ou **Profissional**.
2. Só se o emitente for o profissional, marque **Ativar emissão de nota pelo profissional?** como **Sim**. Com **Não**, a clínica é sempre a emitente.

**3. Serviço cadastrado (de quem emite)**

1. Clínica emitente: em **Financeiro › Asaas › Notas fiscais › Serviços**, clique em **Adicionar serviço**.
2. Profissional emitente: o profissional abre a conta dele (veja Como cadastrar a conta Asaas do profissional (conta filha)) e, após a aprovação, cadastra o serviço em **Personalização › Minha conta Asaas › Notas fiscais › Serviços**.
3. Preencha **Código do serviço municipal**, **Descrição do serviço** (sai impressa na nota), **Alíquota ISS** e, se a prefeitura já usa o emissor nacional, os **Dados IBS/CBS - Reforma Tributária**. Marque um como **Serviço padrão**.

**4. Emissão automática no procedimento (opcional)**

1. Em **Configurações › Procedimentos**, edite o procedimento e, na forma de pagamento, ligue **Emitir nota fiscal automaticamente?**.

**5. No dia a dia:** lançar o recebimento completo antes de finalizar o atendimento. Veja Como emitir nota fiscal e conferir as emissões.

## Regras importantes

- Só existe um serviço padrão por emitente; sem ele, a nota não sai.
- Se o emitente for o profissional e ele não tiver conta Asaas aprovada, a nota não é emitida pela clínica no lugar dele.
- A chave de emissão automática só aparece em modalidade Particular ou convênio sem TISS, com repasse preenchido, e fica bloqueada se o cadastro do Asaas estiver incompleto.
- Cada nota tem um custo, debitado da conta Asaas. Mantenha saldo; o valor fica no contrato e no painel do Asaas.

## Perguntas frequentes

- **Onde atualizo o certificado digital?** No painel do Asaas, em **Notas fiscais › Configurações**.
- **A inscrição municipal dá erro.** Teste sem o dígito final; cada prefeitura tem particularidades.
