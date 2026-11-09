---
titulo: Como configurar o pagamento online
slug: como-configurar-o-pagamento-online
secao: financeiro-e-faturamento
ordem: 80
perfis: Administrador da conta, Administrador da clínica
caminho: Financeiro › Asaas › Dados cadastrais
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Permite que o paciente pague a consulta por Pix ou cartão de crédito, antes (na Agenda Online) ou depois (por um link enviado pela clínica). O valor cai direto na conta Asaas da clínica, aberta dentro da Communicare, e o recebimento é lançado automaticamente no agendamento.

## Quem pode fazer

Gestores (administrador da conta ou da clínica). Como envolve dados bancários e documentos da empresa, o ideal é que o titular da conta faça o cadastro.

## Onde fica

**Financeiro › Asaas › Dados cadastrais**, **Financeiro › Asaas › Cobranças › Formas de recebimento** e **Financeiro › Asaas › Cobranças › Regras**

## Antes de começar

- A conta Asaas precisa ser aberta pela Communicare. Uma conta aberta diretamente no site do Asaas não se integra à plataforma.
- Tenha em mãos os dados da empresa (ou do titular, se pessoa física), endereço e um e-mail e celular válidos.

## Passo a passo

**1. Abrir a conta Asaas da clínica**

1. Acesse **Financeiro › Asaas › Dados cadastrais**.
2. Informe o subdomínio da Agenda Online (até 30 caracteres; não pode ser alterado depois), o **Tipo de empresa**, os dados cadastrais e o endereço.
3. Em **Vincular conta**, escolha a conta do Financeiro onde os recebimentos serão registrados e salve.
4. Abra o e-mail enviado pelo Asaas, defina a senha e, no painel do Asaas, confirme o celular e envie os documentos (documento de identificação e selfie).
5. Aguarde a análise. Quando **Status informações comerciais** e **Status documentação** estiverem como **Aprovado**, siga para o próximo passo.

**2. Ligar o pagamento online**

1. Em **Financeiro › Asaas › Dados cadastrais**, marque **Ativar pagamento online?** como **Sim**.
2. Em **Financeiro › Asaas › Cobranças › Formas de recebimento**, marque as formas aceitas (Pix, crédito à vista, crédito parcelado). Só as marcadas aparecem para o paciente. Em **Editar**, defina o valor mínimo da parcela.
3. Em **Financeiro › Asaas › Cobranças › Regras**, revise o texto das regras de pagamento e cancelamento. Use **Carregar modelo** para partir do padrão, **Ver prévia** para conferir e **Salvar**.
4. Em **Configurações › Procedimentos**, ligue **Pagamento Online** nos procedimentos em que o paciente deve pagar ao agendar pela Agenda Online.

## Regras importantes

- As taxas, o custo por transação e o prazo de recebimento de cada forma aparecem na tela de Formas de recebimento. O Pix cai mais rápido; no crédito, cada parcela cai conforme o prazo do Asaas.
- O valor mínimo da parcela limita o parcelamento. Exemplo: procedimento de 400 com parcela mínima de 200 permite no máximo 2 vezes.
- Com pagamento obrigatório na Agenda Online, o agendamento fica pré-agendado e só é confirmado após o pagamento. Se a reserva expirar, o horário é liberado.
- Ao pagar, o paciente aceita as regras cadastradas.
- Desativar o pagamento online desliga o pagamento online de todos os procedimentos.
- A configuração vale para a conta inteira (todas as clínicas).

## Perguntas frequentes

- **Como envio o link de pagamento depois da consulta?** Abra o agendamento (pela Agenda ou Sala de espera) e clique em **Compartilhar link de pagamento**. Dá para copiar o link ou enviar por WhatsApp ou e-mail (o e-mail só aparece se o paciente tiver e-mail cadastrado). O link pode ser pago por outra pessoa.
- **O link de pagamento não aparece.** Ele só aparece com o agendamento **A receber**, conta Asaas aprovada e pagamento online ativo.
- **O Pix não é gerado.** Há um valor mínimo por cobrança; procedimentos com valor muito baixo dão erro.
- **Meu cadastro ficou em Pendente.** Falta concluir a etapa de documentos no painel do Asaas.
