---
titulo: Como configurar o atendimento imediato
slug: como-configurar-o-atendimento-imediato
secao: configuracoes-do-gestor
ordem: 155
perfis: Administrador da conta
caminho: Conta › Clínicas
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

O atendimento imediato permite começar uma consulta direto da lista de pacientes, sem criar agendamento, sem encaixe e sem passar pela Sala de Espera. É útil para demanda espontânea, quando o paciente chega e o profissional já pode atendê-lo.

## Quem pode fazer

- Configurar: dono da conta ou Admin de Conta (o grupo **Conta** só aparece para esses perfis).
- Usar: profissionais que atendem (nível superior e nível técnico) vinculados ao procedimento escolhido.

## Onde fica

- Configuração: **Conta › Clínicas** › editar a clínica › **Dados cadastrais** › campo **Procedimento do atendimento imediato**
- Uso: **Pacientes** › botão **Iniciar atendimento** na linha do paciente

## Antes de começar

- Tenha um procedimento cadastrado em **Configurações › Procedimentos** para esse tipo de atendimento, com pelo menos uma modalidade de pagamento.
- Os profissionais que vão usar o recurso precisam estar vinculados a esse procedimento como executores.

## Passo a passo

1. Acesse **Conta › Clínicas** e clique para editar a clínica.
2. Em **Dados cadastrais**, localize **Procedimento do atendimento imediato** e escolha o procedimento.
3. Em **Modalidade de pagamento**, escolha uma das modalidades cadastradas nesse procedimento (por exemplo, particular ou um convênio).
4. Salve os dados da clínica.
5. Confira os profissionais: em **Configurações › Procedimentos**, edite o procedimento escolhido e verifique, em **Profissionais**, se todos que vão atender estão na lista. Se faltar alguém, adicione.
6. Pronto: em **Pacientes**, aparece o botão verde **Iniciar atendimento** na coluna **Ações** de cada paciente.

## Como usar no dia a dia

1. Em **Pacientes**, busque o paciente (cadastre-o antes, se for novo).
2. Clique em **Iniciar atendimento**.
3. O sistema cria o atendimento e abre o prontuário (SOAP). Atenda e finalize normalmente, como em uma consulta agendada.

## Regras importantes

- Só é possível vincular um procedimento de atendimento imediato por clínica.
- Sem procedimento configurado (opção **Nenhum**), o botão **Iniciar atendimento** não aparece.
- O atendimento usa o procedimento e a modalidade de pagamento definidos na clínica. Para lançar valores ou repasse, siga as mesmas regras de um atendimento comum.
- A recepção não usa o botão, porque não tem acesso ao prontuário.

## Perguntas frequentes

- **O botão Iniciar atendimento não aparece em Pacientes. Por quê?** Confira se a clínica tem o **Procedimento do atendimento imediato** preenchido e salvo.
- **Cliquei no botão e apareceu erro.** Normalmente o profissional não está vinculado ao procedimento escolhido. Inclua-o em **Configurações › Procedimentos** › **Profissionais**.
- **O atendimento imediato aparece na agenda e nos relatórios?** Sim, ele é registrado como um atendimento da clínica, com o procedimento configurado.
- **Atendimento imediato é o mesmo que emitir documento sem agendamento?** Não. Aqui você faz um atendimento completo no SOAP; para só emitir um documento, use o tutorial de documentos sem agendamento.
