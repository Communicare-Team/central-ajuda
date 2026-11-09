---
titulo: Como configurar o SOAP
slug: como-configurar-o-soap
secao: configuracoes-do-gestor
ordem: 140
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Configurar SOAP
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Cada seção do prontuário SOAP (Subjetivo, Objetivo, Avaliação e Plano) é formada por blocos, como História atual, Exame físico, Sinais vitais ou Receitas. Nesta tela o gestor define a ordem desses blocos e para quais profissões e especialidades cada um aparece. Assim, cada profissional vê no atendimento só o que faz sentido para a área dele.

## Quem pode fazer

Gestores: Admin de Conta e Admin de Clínica.

## Onde fica

**Configurações › Configurar SOAP**

## Antes de começar

- As profissões e especialidades dos profissionais precisam estar corretas no cadastro de cada usuário (**Conta › Usuários**), porque são elas que aparecem na lista de escolha.
- Se for usar formulários próprios da clínica, crie-os antes em **Configurações › Formulários personalizados** (disponível conforme o plano contratado).

## Passo a passo

1. Acesse **Configurações › Configurar SOAP**. A tela mostra os blocos separados por seção do SOAP.
2. Para mudar a ordem, clique nos três tracinhos à esquerda do bloco e arraste para a posição desejada dentro da seção.
3. Para definir quem vê um bloco, clique em **Profissão - Especialidade** ao lado dele e marque as combinações desejadas (por exemplo, "Psicólogo" ou "Médico - Ginecologia"). A escolha é salva ao fechar a lista; aparece a mensagem "Especialidades salvas com sucesso!".
4. Depois de reorganizar, clique em **Salvar** para gravar a nova ordem. A mensagem "Ordem dos formulários salva com sucesso!" confirma.

## Regras importantes

- Alguns blocos do sistema são fixos e não podem ser movidos; eles mostram um cadeado com o aviso "Este formulário não pode ser reposicionado".
- Formulários criados pela clínica aparecem com "(modelo personalizado)" ao lado do nome. Um formulário personalizado só aparece no atendimento depois de configurado aqui para as profissões e especialidades certas.
- Blocos padrão de cada seção:
  - **Subjetivo**: História atual, Antecedentes, Lembretes e Prontuários anteriores.
  - **Objetivo**: Exame físico, Oftalmologia, Medidas, Sinais vitais, Escalas, Odontograma, Resultados e Procedimentos.
  - **Plano**: Exames, Receitas, Encaminhamento, Orientações, Atestados, Observações e Cuidados.
- A configuração vale para toda a conta. Ela muda a tela do atendimento, não apaga registros já feitos.
- O profissional de nível técnico só acessa Subjetivo, Objetivo e Validação; a recepção não entra no SOAP.

## Configurar SOAP x modelos de prontuário

- **Configurar SOAP**: define quais blocos aparecem e em que ordem.
- **Configurações › Modelos › SOAP**: textos prontos da clínica (anamnese, atestado, pedido de exames etc.) que valem para todos os profissionais.
- **Personalização › Meus modelos › SOAP**: modelos de cada profissional. Veja o tutorial de modelos de prontuário.

## Perguntas frequentes

- **Criei um formulário personalizado e ele não aparece no atendimento. Por quê?** Falta liberá-lo em **Configurar SOAP** para a profissão e especialidade do profissional.
- **Quero que o Odontograma apareça só para dentistas. Dá?** Sim, selecione apenas a profissão correspondente em **Profissão - Especialidade** no bloco Odontograma.
- **Posso mover um bloco de uma seção para outra (do Subjetivo para o Objetivo)?** Para formulários personalizados, altere o **Local do SOAP** no próprio formulário. Os blocos do sistema ficam na seção original.
