---
titulo: Como configurar um disparo automático de mensagens no WhatsApp
slug: como-configurar-um-disparo-automatico-de-mensagens
secao: communicare-conversas
ordem: 9
perfis: Quem tem acesso ao menu Whatsapp
caminho: Whatsapp › Disparos
video:
video_rotulo:
atualizado: 2026-11-01
---
## Para que serve
Enviar mensagens automáticas pelo WhatsApp em momentos-chave: quando a consulta é marcada, antes da consulta (confirmação e lembrete), depois do atendimento, em caso de falta, no aniversário do paciente e outros.

## Quem pode fazer
Usuários com acesso ao menu Whatsapp.

## Onde fica
**Whatsapp › Disparos**

## Antes de começar
Você precisa de um template aprovado pela Meta (veja "Como criar um template de mensagem do WhatsApp").

## Passo a passo
1. Acesse **Whatsapp › Disparos** e crie um novo disparo.
2. Em **Gatilho**, escolha o evento que dispara a mensagem. O campo tem busca: digite, por exemplo, "agend".
3. Em **Modelo**, escolha o template aprovado.
4. Em **Ação primária**, escolha quando enviar: minutos, horas ou dias, antes ou depois do evento.
5. Em **Quantidade**, informe o número (por exemplo, 24 para "24 horas antes").
6. Salve.

## Regras importantes
- Gatilhos de **agendamento** e **teleconsulta** aceitam envio antes ou depois. Gatilhos de **atendimento finalizado**, **cadastro de paciente** e **falta** aceitam só depois.
- **Aniversário** é sempre enviado no próprio dia.
- Com a **Quantidade** vazia ou zero, a mensagem não é agendada: ela sai na hora do evento. Use isso para mandar uma mensagem assim que a consulta é marcada.
- Se o horário calculado já passou há mais de 1 hora, o disparo é **cancelado**. Exemplo: confirmação configurada para 24 horas antes e consulta marcada para daqui a 3 horas.
- Se o horário calculado passou há menos de 1 hora, a mensagem sai na hora.
- Para trocar a mensagem de um disparo, edite o disparo e escolha outro modelo.

## Perguntas frequentes
### Tenho o Communicare Conversas. Configuro a confirmação em Configurações › Mensageria?
Não. Com o Conversas, as mensagens automáticas são configuradas aqui, com template e disparo. A tela de Mensageria vale para contas sem o Conversas.

### Por que um disparo aparece como Cancelado?
Em geral porque a consulta foi marcada depois do prazo do disparo. Veja a regra de 1 hora acima.

### Como mando uma mensagem assim que a consulta é marcada?
Use um gatilho de agendamento e deixe a Quantidade vazia.
