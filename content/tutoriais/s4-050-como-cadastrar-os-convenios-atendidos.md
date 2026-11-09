---
titulo: Como cadastrar os convênios atendidos
slug: como-cadastrar-os-convenios-atendidos
secao: configuracoes-do-gestor
ordem: 50
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Convênios
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Cadastra os convênios e planos que a clínica atende, para que eles apareçam no agendamento, na Agenda Online e no faturamento. Também serve para criar acordos com preço diferenciado (parcerias, empresas, descontos) sem emitir guia.

## Quem pode fazer

Gestores: administrador da conta ou administrador da clínica.

## Onde fica

**Configurações › Convênios** › botão **Adicionar** (ou **Adicionar da lista da ANS**)

## Antes de começar

Decida se o convênio vai usar o faturamento TISS da Communicare:

- **Com Fatura TISS**: a clínica emite guias (consulta ou SP-SADT) e envia os lotes ao convênio. O recebimento não é lançado no agendamento.
- **Sem Fatura TISS**: não emite guia e funciona como particular, com valor próprio. É o caminho para parcerias, empresas conveniadas, vouchers e descontos. O recebimento precisa ser lançado no agendamento para calcular o repasse.

## Passo a passo

1. Acesse **Configurações › Convênios** e clique em **Adicionar**. Para puxar os dados oficiais da operadora, use **Adicionar da lista da ANS**.
2. Em **Dados da operadora**, preencha o **Nome fantasia**.
3. Se for faturar pela Communicare, ligue **Fatura TISS?** e preencha também razão social, CNPJ, modalidade, **Nº ANS**, **Versão da TISS** usada pelo convênio e **Motivo de encerramento padrão**.
4. Com TISS, em **Dados do executante**, clique em **Adicionar executante** e informe o contratado, CNES, código na operadora e **Nº guia operadora**. Se o convênio é novo para a clínica, use 0 ou deixe em branco. Se já emitiu guias por fora, informe o último número usado.
5. Em **Planos**, clique em **Adicionar** e cadastre pelo menos um plano. Pode ser um único plano "Geral".
6. Se quiser, envie um **Fundo de tela virtual do convênio** para usar na teleconsulta.
7. Clique em **Salvar**.

## Depois de cadastrar

- Vincule o convênio aos procedimentos: em **Configurações › Procedimentos**, edite o procedimento e, em modalidade de pagamento, adicione uma linha **Convênio** com o convênio, o plano e o valor (um por plano).
- Para convênio com TISS, informe o código TUSS no procedimento. Sem ele, a guia sai incompleta.
- No cadastro de cada paciente, adicione o convênio, o plano e a carteirinha. Sem isso, o agendamento só mostra a opção particular.

## Regras importantes

- Agendamento de convênio sem **Fatura TISS** ligado é tratado como particular.
- Procedimento do tipo consulta gera guia de consulta. Para gerar SP-SADT, o procedimento precisa ser do tipo exame/procedimento.
- Um plano não pode ser removido se tiver procedimentos associados.
- Para impedir um convênio em uma clínica específica, use **Convênios com Restrição** em **Conta › Clínicas › Editar**.

## Perguntas frequentes

- **Agendei por convênio e virou particular. Por quê?** O convênio está com **Fatura TISS?** desligado.
- **Os procedimentos do convênio não fazem repasse.** Em convênio sem TISS, o repasse só é calculado depois que o recebimento é lançado no agendamento.
- **Posso dar desconto para pacientes de uma parceria?** Sim. Cadastre um convênio sem TISS com o nome da parceria e coloque um valor menor na modalidade desse convênio no procedimento.
- **O convênio pediu SP-SADT e saiu guia de consulta.** Confira se o procedimento está cadastrado como exame/procedimento.
