---
titulo: Como criar a fila de atendimento online
slug: como-criar-a-fila-de-atendimento-online
secao: configuracoes-do-gestor
ordem: 150
perfis: Administrador da conta, Administrador da clínica
caminho: Filas › Configuração de filas
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

A fila de atendimento online funciona como um pronto atendimento por teleconsulta: o paciente entra na fila pela Agenda Online, sem horário marcado, e é chamado pelo próximo profissional disponível. A clínica pode ter várias filas, por exemplo adulto, infantil ou saúde mental.

## Quem pode fazer

Gestores (Admin de Conta e Admin de Clínica). Os profissionais usam apenas a aba **Minhas filas** para atender.

## Onde fica

**Filas › Configuração de filas** (o menu **Filas** é o último item do menu lateral)

## Antes de começar

- Crie um procedimento do tipo teleconsulta para a fila em **Configurações › Procedimentos**. Ele define o valor cobrado e o repasse. Sem nenhum procedimento de teleconsulta na conta, não é possível criar fila.
- Inclua como profissionais executores desse procedimento todos que vão atender a fila. Quem não está no procedimento não consegue atender aquela fila.
- Dica: crie um procedimento separado para cada fila. Os relatórios mostram o procedimento, não o nome da fila.

## Passo a passo

1. Acesse **Filas › Configuração de filas** e clique em **Nova Fila**.
2. Preencha **Nome da Fila** (uso interno) e escolha a **Cor da barra**.
3. Preencha **Nome para Paciente**: é o nome que aparece na Agenda Online.
4. Em **Descrição**, explique ao paciente quem é atendido nessa fila e as regras.
5. Em **Procedimento de Teleconsulta**, escolha o procedimento criado para a fila.
6. Ligue **Mostrar fila na agenda online**.
7. Se a fila for para uma faixa etária, preencha **Idade mínima** e **Idade máxima para atendimento**.
8. Para limitar o funcionamento, ligue **Restringir horário de acesso**, escolha os dias da semana, a hora de início e a de fim. Use **Adicionar faixa de horário** para mais de um período. Com a opção desligada, a fila fica aberta 24 horas.
9. **Configuração de Webhook** é opcional e serve para a equipe de TI da clínica receber os dados da fila.
10. Clique em **Salvar**.

## Como editar e testar

- Na coluna **Ações**: editar, ver o histórico de alterações, copiar o link da fila (para divulgar no site da clínica) e copiar o identificador usado em integrações.
- Para testar, use a opção de adicionar um paciente de teste à fila e abra o link em outra aba.

## Regras importantes

- Os horários seguem sempre o horário de Brasília. Fora da faixa configurada, o paciente não consegue entrar.
- Se a fila não aparecer na Agenda Online, confira também **Configurações › Agenda online** (permissão para exibir a fila de pronto atendimento).
- Atendimento de fila entra na agenda como encaixe.
- Se o procedimento tem valor, o paciente paga e aceita o termo de consentimento antes de entrar na fila. Com valor zero, entra direto.
- O envio de dados configurado em **Configuração de Webhook** é desativado automaticamente se falhar ou demorar mais de 5 segundos.
- Para mandar o paciente a outra fila ao final do atendimento, configure o campo **Fila** no desfecho (**Configurações › Desfechos**).
- Em **Gestão de filas**, o gestor acompanha quem está esperando, quem foi atendido, quem desistiu e qual profissional chamou.

## Perguntas frequentes

- **O paciente não consegue entrar na fila. O que conferir?** Horário de acesso (Brasília), faixa de idade, a opção **Mostrar fila na agenda online** e se o pagamento foi concluído.
- **O profissional não vê pacientes na fila.** Confirme se ele é executor do procedimento vinculado à fila.
- **Posso divulgar a fila no site?** Sim, use o link copiado em **Ações**.
