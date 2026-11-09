---
titulo: Como criar desfechos de consulta
slug: como-criar-desfechos-de-consulta
secao: configuracoes-do-gestor
ordem: 130
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Desfechos
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

O desfecho registra como terminou cada atendimento (por exemplo, "Atendimento concluído", "Retorno agendado", "Encaminhado"). Ele vira indicador nos relatórios, pode mandar o paciente para outra fila e define se o atendimento foi conclusivo ou não.

## Quem pode fazer

Gestores: Admin de Conta e Admin de Clínica criam e editam desfechos. Os profissionais escolhem o desfecho ao finalizar o atendimento.

## Onde fica

**Configurações › Desfechos** (abas **Ativos** e **Inativos**)

## Passo a passo

1. Acesse **Configurações › Desfechos** e clique em **Adicionar**.
2. Preencha **Nome** (obrigatório), por exemplo "Atendimento concluído".
3. Preencha **Descrição** (obrigatória). Use para orientar o profissional sobre quando escolher esse desfecho.
4. Em **Fila**, escolha para qual fila o paciente deve ser levado ao final do atendimento, ou deixe **Nenhum redirecionamento**. Só se aplica a quem usa filas de atendimento online.
5. Marque **Desfecho inconclusivo** se esse desfecho representar um atendimento que não se completou (por exemplo, queda de conexão ou problema técnico).
6. Clique em **Salvar**.

Crie quantos desfechos precisar. Para tirar um de uso, inative-o; ele vai para a aba **Inativos** e pode ser reativado depois. O botão **Histórico** mostra quem criou ou alterou cada desfecho.

## O que muda quando o desfecho é inconclusivo

- O paciente pode reagendar ou cancelar o agendamento depois do atendimento pela Agenda Online (e, se pagou online, pedir o estorno).
- A nota fiscal automática não é emitida.
- Na fila de atendimento online, o pagamento ao profissional só é confirmado com desfecho conclusivo.
- Na Sala de Espera o atendimento aparece como "inconclusivo".

## Regras importantes

- Com desfechos ativos cadastrados, o profissional só consegue finalizar o atendimento depois de escolher um desfecho no resumo final.
- Só desfechos ativos aparecem para escolha. Se o atendimento já tinha desfecho, ele vem pré-selecionado.
- Redirecionamento para fila: o paciente só entra na nova fila se continuar na videochamada até o profissional finalizar. Se sair antes, não é redirecionado.
- O Admin de Conta pode trocar o desfecho de um atendimento finalizado pela folha de rosto do paciente (ícone de estetoscópio, **Editar desfecho clínico**).

## Onde ver os desfechos

- No histórico do agendamento.
- No relatório administrativo, coluna **Desfecho** (marque a coluna no filtro de campos; dá para exportar em planilha).

## Perguntas frequentes

- **O profissional não consegue finalizar o atendimento. O que fazer?** Provavelmente falta escolher o desfecho no resumo final.
- **Escolhi o desfecho errado. Dá para corrigir?** Sim. O Admin de Conta troca pela folha de rosto do paciente, sem precisar acionar o suporte.
- **Onde está a opção "Permitir reagendamento"?** Ela passou a se chamar **Desfecho inconclusivo**.
- **O paciente com desfecho inconclusivo recebe a pesquisa NPS?** Hoje sim, a pesquisa pode ser enviada mesmo com desfecho inconclusivo.
