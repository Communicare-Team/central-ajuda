---
titulo: Como criar equipes e distribuir os atendimentos
slug: como-criar-equipes-e-distribuir-os-atendimentos
secao: communicare-conversas
ordem: 16
perfis: Administrador da conta
caminho: Conversas › Ajustes › Equipes
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Separar o atendimento por áreas (por exemplo, recepção, financeiro, enfermagem) e controlar quem vê cada conversa. Com a distribuição ligada, cada conversa nova vai para uma pessoa por vez, em rodízio, evitando que duas pessoas respondam o mesmo paciente ou que alguém fique sem resposta.

## Quem pode fazer

Usuário com perfil **Administrador** no Conversas.

## Onde fica

Botão verde **Conversas** no topo do sistema › **Ajustes** › **Equipes**.

## Antes de começar

- Libere o acesso das pessoas ao Conversas (veja "Como liberar o acesso dos usuários ao Communicare Conversas").
- Configure o horário de atendimento.

## Passo a passo

### Criar uma equipe

1. Em **Equipes**, clique em **+ Novo**.
2. Dê um nome à equipe.
3. Indique se é a **equipe padrão**: ela recebe as conversas que não têm outro destino.
4. Escolha quem vê os atendimentos:
   - **Todos:** conversas concluídas ficam visíveis para todos.
   - **Equipe:** concluídas visíveis só para a equipe.
   - **Atendente:** só o responsável e os supervisores veem. Indicado para assuntos sensíveis.
5. Associe as pessoas como **Usuário**, **Supervisor** ou ambos.
6. Clique em **Salvar**.

### Ligar a distribuição (rodízio)

1. Habilite o app **Distribuição de Atendimentos** em **Apps**.
2. Em **Equipes**, clique em **Alterar** na equipe e ligue a chave de distribuição.
3. Defina o **Limite de tempo para realizar transbordo** (quanto tempo a pessoa tem para assumir antes de passar para a próxima) e o **Tempo limite máximo** (depois dele, a conversa fica disponível para a equipe toda). Use valores diferentes nos dois campos.
4. Salve.

## Regras importantes

- Toda conversa precisa estar em uma equipe. Uma pessoa pode participar de várias.
- **Supervisor** vê e atua em todas as conversas da equipe, mas **não entra no rodízio**. Se ele também precisa receber conversas, associe-o como Usuário e Supervisor.
- A ordem do rodízio segue a **data de cadastro do usuário** e não pode ser mudada. Quem entra depois fica no fim da fila. Para ver a ordem, abra a equipe e clique em **Ver ordem**.
- **Disponibilidade** não é "estar online": serve para tirar alguém do rodízio em férias ou licença, e vale para todas as equipes da pessoa ao mesmo tempo.
- Se todos estiverem indisponíveis, a conversa vai para a equipe inteira com o aviso "Atendimento não distribuído".
- Fora do horário de atendimento, com resposta automática desligada, a conversa espera sem transbordo.
- Ao excluir uma equipe com conversas abertas, o sistema pergunta se deve concluí-las ou movê-las.

## Perguntas frequentes

- **A secretária nova nunca recebe conversa primeiro.** O rodízio segue a data de cadastro; ela entrou no fim da fila.
- **O supervisor não recebe conversas automaticamente.** Supervisores ficam fora da distribuição.
- **Marquei uma pessoa como indisponível e ela saiu de todas as equipes.** A disponibilidade vale para todas as equipes dela.
- **O transbordo não acontece.** Confira se os dois tempos estão diferentes.
