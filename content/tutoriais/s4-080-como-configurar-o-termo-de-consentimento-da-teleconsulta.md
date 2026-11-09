---
titulo: Como configurar o termo de consentimento da teleconsulta
slug: como-configurar-o-termo-de-consentimento-da-teleconsulta
secao: configuracoes-do-gestor
ordem: 80
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Teleconsulta
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Define o texto do termo de consentimento que o paciente aceita antes da teleconsulta. O aceite fica registrado como documento no prontuário, dando respaldo à clínica.

## Quem pode fazer

Gestores: administrador da conta ou administrador da clínica. O item só aparece quando a conta tem assinatura ativa.

## Onde fica

**Configurações › Teleconsulta** › bloco **Termo de consentimento**

## Antes de começar

- Toda conta já vem com um termo padrão, revisado pelo jurídico da Communicare. Se ele atende a clínica, não é preciso mudar nada.
- Se a clínica tem um texto próprio, revise-o com o seu jurídico antes de colar no sistema.

## Passo a passo

1. Acesse **Configurações › Teleconsulta**.
2. No editor do **Termo de consentimento**, ajuste o texto. O editor aceita formatação (fonte, tamanho, cor).
3. Para incluir dados do paciente, clique no ponto do texto e insira um dos campos dinâmicos. O sistema troca pelo dado real na hora da consulta:
   - %NOME% (primeiro nome) e %NOMECOMPLETO%
   - %NASCIMENTO% e %IDADE%
   - %CPF%
4. Se tiver mais de um texto, use **Carregar modelo** para escolher um modelo salvo, ou crie um novo informando o **Nome do modelo**. Marque **Modelo Padrão da conta** no que deve ser usado por padrão.
5. Clique em **Prévia** para ver como o termo fica preenchido.
6. Se quiser que o paciente aceite o termo já ao agendar pela Agenda Online, ligue **Exibir caixa de seleção para aceitação do termo no agendamento**.
7. Salve. Aparece a mensagem "Configuração atualizada com sucesso!".

## Como o termo chega ao paciente

- **No agendamento online:** com a caixa de aceite ligada, o paciente lê o termo já preenchido com os dados dele e precisa marcar o aceite para continuar (antes do pagamento, quando houver).
- **Na teleconsulta:** o paciente aceita o termo antes de entrar na chamada.
- O aceite gera um documento registrado no atendimento, que pode ser consultado pelos profissionais em **Pacientes** › folha de rosto › **Percurso assistencial**, no card da consulta.

## Regras importantes

- O consentimento é verificado por agendamento, não uma vez só por paciente.
- A caixa de aceite na Agenda Online é um interruptor separado do texto: mudar o texto não liga nem desliga a exibição.
- O termo não pode ficar em branco ("Texto do termo é obrigatório").
- Recepcionistas e perfis administrativos não acessam o prontuário, então não veem o termo aceito.

## Perguntas frequentes

- **Preciso escrever o termo do zero?** Não. O modelo padrão já cobre as cláusulas usuais (tecnologia e riscos, confidencialidade, alternativas, emergências, entre outras). Você pode só ajustar.
- **Onde encontro o termo que o paciente aceitou?** No **Percurso assistencial** do paciente, no card da consulta.
- **E para consultas presenciais?** Este termo é da teleconsulta. Para termos presenciais, use os formulários da clínica.
- **Posso ter um termo diferente para cada tipo de atendimento?** É possível salvar vários modelos, mas o que vale para a conta é o marcado como padrão.
