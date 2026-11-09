---
titulo: Como fazer o faturamento TISS e SADT
slug: como-fazer-o-faturamento-tiss-e-sadt
secao: financeiro-e-faturamento
ordem: 130
perfis: Administrador da conta, Recepção
caminho: Financeiro › Faturamento TISS › Guias TISS
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Organiza a cobrança dos atendimentos de convênio no padrão TISS da ANS: a clínica emite a guia no atendimento, junta as guias em lotes e baixa o arquivo XML (ou TXT) para enviar à operadora.

## Quem pode fazer

A guia é emitida no agendamento por quem lança recebimentos. Fechar e baixar lotes é do dono ou administrador da conta.

## Onde fica

- Emissão: no agendamento (**Emitir guia de consulta** ou **Emitir guia SADT**) e na Sala de espera (**Emitir guia SADT**, para guia avulsa)
- Lotes: **Financeiro › Faturamento TISS › Guias TISS** e **Financeiro › Faturamento TISS › Administrar lotes**

## Antes de começar

- Convênio com **Fatura TISS?** ligado e dados da operadora e do contratado preenchidos. Veja Como cadastrar os convênios atendidos.
- Procedimento com o código TUSS na modalidade do convênio. Tipo **Consulta** gera guia de consulta; para guia SADT, o procedimento precisa ser **Exame/Procedimento** e agendável, com os **Itens de terapia**. Veja Como criar os procedimentos de consultas e exames.
- Profissional com CBO e conselho no cadastro.

## Passo a passo

**1. Emitir a guia**

1. Abra o agendamento do convênio (pela Agenda ou pela Sala de espera, em **Lançar recebimento**).
2. Clique em **Emitir guia de consulta** ou **Emitir guia SADT**. Os dados do paciente e do procedimento vêm preenchidos; a carteirinha vem do cadastro do paciente.
3. Complete o que faltar (número da guia na operadora, senha e validade da autorização, contratado) e clique em **Emitir**.
4. Imprima a guia para colher a assinatura do paciente.

**2. Fechar o lote**

1. Em **Financeiro › Faturamento TISS › Guias TISS**, filtre por **Convênio**, **Tipo de guia** e período. Use o filtro de lote para ver as guias ainda sem lote.
2. Marque as guias (ou **Selecionar todos**) e clique em **Fechar lote**. Para incluir em um lote aberto, use **Inserir em lote existente**.
3. Faça lotes separados para guias de consulta e SADT.

**3. Baixar e enviar**

1. Em **Financeiro › Faturamento TISS › Administrar lotes**, filtre pelo convênio e mês de referência.
2. Baixe o XML (ou **Baixar TXT**, se a operadora exigir) e envie pelo site da operadora.
3. Em **Editar**, registre protocolo e número da nota fiscal.

## Regras importantes

- Convênio com TISS não tem recebimento lançado no agendamento: a cobrança vai pela guia. Convênio sem TISS funciona como particular e exige lançar o recebimento.
- Exame feito junto da consulta sai em guia SADT separada.
- Agendamento com guia autorizada não pode ser cancelado: cancele a guia antes.
- Cada fechamento aceita até 100 guias.
- Na lista de guias, atualize o status manualmente (por exemplo, autorizada, glosada, paga) para a equipe acompanhar o retorno da operadora.
- O envio à operadora é feito por você, no site dela.

## Perguntas frequentes

- **Como troco o solicitante da SADT?** Abra a guia, cancele, ajuste os dados na guia que reabre preenchida e emita de novo.
- **O convênio pede SADT, mas sai guia de consulta.** O procedimento está como Consulta; cadastre-o como **Exame/Procedimento**.
- **Erro ao emitir: falta código.** Complete o código na operadora do contratado (convênio) ou o CBO do profissional.
- **A operadora rejeitou o XML.** Fale com o suporte pelo botão **Falar com o suporte**, enviando o retorno da operadora.
