---
titulo: Como configurar a avaliação NPS
slug: como-configurar-a-avaliacao-nps
secao: configuracoes-do-gestor
ordem: 120
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Gestão do NPS
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

A avaliação NPS pergunta ao paciente, depois do atendimento, de 0 a 10 o quanto ele recomendaria a clínica, com espaço para comentário. Com isso o gestor acompanha a satisfação por profissional e por procedimento.

## Quem pode fazer

Gestores: Admin de Conta e Admin de Clínica. Outros usuários veem o item, mas recebem aviso de que não têm permissão.

## Onde fica

**Configurações › Gestão do NPS**

## Antes de começar

- A Agenda Online precisa estar configurada (**Configurações › Agenda online**). É por ela que o paciente abre e responde a pesquisa; sem isso, a resposta não é registrada.
- Se a conta tem mais de uma clínica, a configuração é feita em cada clínica.

## Passo a passo

1. Acesse **Configurações › Gestão do NPS**.
2. No bloco **Avaliação de NPS - Atendimento Presencial**, ligue **Enviar avaliação de NPS ao final do atendimento presencial?**.
3. Escolha a frequência (obrigatória):
   - Apenas no primeiro atendimento do paciente por um novo profissional;
   - Apenas no primeiro atendimento do paciente na clínica;
   - Em todo atendimento, mas com um intervalo mínimo de 90 dias;
   - Em todo atendimento, independente do intervalo entre as consultas.
4. Em **Exceções à regra (Procedimentos Presenciais)**, marque os procedimentos que não devem gerar pesquisa (por exemplo, procedimentos internos).
5. No bloco **Avaliação de NPS - Teleconsulta**, ligue **Mostrar a avaliação ao final do atendimento de cada teleconsulta?** e, se quiser, defina as **Exceções à regra (Procedimentos de Teleconsulta)**.
6. Se quiser reforçar, ligue **Enviar avaliação por e-mail caso o paciente não responda após 30 minutos**.
7. Clique em **Salvar**.

## Como enviar o NPS pelo WhatsApp

Além do e-mail, a clínica pode mandar o link da pesquisa por WhatsApp:

1. Em **Whatsapp › Templates**, crie um template de avaliação e use o dado dinâmico do link do NPS do atendimento, no texto ou em um botão (por exemplo, "Avaliar agora"). O template passa pela aprovação da Meta.
2. Em **Whatsapp › Disparos**, crie um gatilho de finalização de atendimento (qualquer atendimento, procedimento específico, primeiro atendimento na clínica ou primeiro atendimento com o profissional).
3. Escolha o template e quantas horas depois da finalização enviar (0 = na hora). Salve.

## Regras importantes

- A pesquisa é enviada quando o profissional finaliza o atendimento. Pré-consulta e edição de atendimento já finalizado não geram nova pesquisa.
- Presencial e teleconsulta são configurações independentes: ligar uma não liga a outra.
- Na teleconsulta, ao encerrar a chamada, o paciente é levado direto para a avaliação.
- A pesquisa por e-mail usa o e-mail do cadastro do paciente; sem e-mail, ela não chega.

## Onde ver os resultados

Em **Dashboard › aba NPS**: filtre por clínica, profissionais, procedimentos, tipo de nota (promotores, neutros, detratores) e período, e clique em **Gerar relatório**. Aparecem o score, a distribuição das notas e a tabela com profissional, procedimento, nota e comentário.

## Perguntas frequentes

- **Ativei o NPS, mas não aparece nenhuma resposta. Por quê?** Confira se a Agenda Online está configurada, se o procedimento não está nas exceções e se a frequência escolhida não exclui aquele atendimento.
- **Dá para não enviar NPS em retornos ou procedimentos internos?** Sim, marque esses procedimentos em **Exceções à regra**.
- **O paciente recebe a pesquisa a cada consulta?** Só se a frequência for "Em todo atendimento, independente do intervalo".
