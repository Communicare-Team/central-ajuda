---
titulo: Como configurar as permissões dos usuários
slug: como-configurar-as-permissoes-dos-usuarios
secao: configuracoes-do-gestor
ordem: 40
perfis: Administrador da conta
caminho: Conta › Usuários
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Define o que cada pessoa da equipe enxerga e pode fazer na Communicare: quem administra a conta, quem configura cada clínica, quem vê valores, quais pacientes e agendas cada um acessa.

## Quem pode fazer

Dono ou administrador da conta.

## Onde fica

**Conta › Usuários** › ícone **Editar** (lápis) do usuário

## Antes de começar

- O usuário precisa ter aceitado o convite. Enquanto estiver pendente, as alterações de permissão não são salvas (aparece "Usuário pendente de ativação").
- A **Função** (Recepcionista/Administrativo, Nível técnico ou Nível superior) já define o acesso ao prontuário: recepção nunca entra no prontuário; nível técnico acessa só Subjetivo, Objetivo e Validação.

## Passo a passo

1. Acesse **Conta › Usuários** e clique em **Editar** no usuário.
2. No topo do cadastro, ligue ou desligue as permissões:
   - **Admin de Conta**: acesso total, como o dono, incluindo os menus **Conta** e **Financeiro** e todas as clínicas.
   - **Restrição de valores**: esconde os valores dos procedimentos, a lista de pacientes e os relatórios.
   - **Restrição de pacientes**: o usuário só vê os pacientes das clínicas de referência às quais está vinculado e perde acesso a relatórios, dashboard e ao botão **+** do topo.
   - **Acesso aos Dashboards**: libera os dashboards para quem não é administrador.
   - **Restrição por convênio**: o usuário só vê dados dos convênios selecionados.
3. Em **Acesso às clínicas**, ligue as clínicas em que a pessoa trabalha. Ligue **Admin** na clínica para que ela possa usar o menu **Configurações** daquela clínica (horários, bloqueios, procedimentos, convênios, mensageria, impressos e outros).
4. Em **Acesso à teleinterconsulta**, marque **Solicitante**, **Solicitado** ou os dois, se a conta usa teleinterconsulta.
5. Na coluna da direita, ajuste **Quem eu consigo ver a agenda** e **Quem vê a minha agenda**.
6. Clique em **Salvar**.

## O que cada nível acessa

| Permissão | Menus liberados |
| --- | --- |
| Sem administração | Agenda, sala de espera, pacientes e o que a função permitir |
| Admin de clínica | Também **Configurações** e **Financeiro** daquela clínica (no Financeiro, receitas e despesas, TISS e descontos ficam só para admin de conta) |
| Admin de conta | Tudo, incluindo **Conta** (usuários, clínicas, assinatura) e todas as clínicas |

## Regras importantes

- Quem não é gestor ainda vê os itens de **Configurações** no menu, mas recebe um aviso de que não tem permissão ao abrir.
- Com **Admin de Conta** ligado, os interruptores de clínica ficam travados, porque o acesso já é total.
- Para usar **Restrição de pacientes**, cada paciente precisa ter a clínica de referência informada no cadastro dele (campo **Referências**).
- Exportar prontuários exige perfil administrador.

## Perguntas frequentes

- **A secretária não consegue abrir o prontuário.** É o comportamento esperado para a função Recepcionista/Administrativo.
- **O usuário não vê o Financeiro.** Ele precisa ser Admin de alguma clínica ou Admin de Conta.
- **Um profissional está vendo relatórios e dashboards que não deveria.** Ligue **Restrição de valores** ou **Restrição de pacientes** no cadastro dele.
- **O usuário não consegue filtrar a lista de cuidados por um profissional.** Dê a ele acesso à agenda desse profissional em **Quem eu consigo ver a agenda**.
- **Qual a diferença entre admin de conta e admin de clínica?** O admin de clínica configura a clínica. Só o admin de conta inclui usuários, cria clínicas e mexe na assinatura.
