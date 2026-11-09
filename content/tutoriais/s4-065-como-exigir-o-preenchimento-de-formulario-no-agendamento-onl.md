---
titulo: Como exigir o preenchimento de formulário no agendamento online
slug: como-exigir-o-preenchimento-de-formulario-no-agendamento
secao: configuracoes-do-gestor
ordem: 65
perfis: Administrador da conta, Administrador da clínica
caminho: Configurações › Procedimentos
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Faz o paciente responder um formulário (por exemplo, uma triagem ou questionário de saúde) antes de concluir o agendamento pela Agenda Online. O profissional recebe as respostas prontas para validar no início do atendimento.

## Quem pode fazer

Gestores: administrador da conta ou administrador da clínica. Recurso disponível conforme o plano contratado: quando o plano não inclui, a opção não aparece no procedimento.

## Onde fica

- Formulário: **Configurações › Formulários personalizados**
- Exigência no agendamento: **Configurações › Procedimentos** › editar o procedimento
- Acesso dos profissionais: **Configurações › Configurar SOAP**

## Antes de começar

- A Agenda Online precisa estar configurada e o procedimento precisa aparecer nela (profissional executor e opção **Agenda online** ligados).

## Passo a passo

### 1. Criar o formulário

1. Acesse **Configurações › Formulários personalizados** e adicione um formulário.
2. Informe o nome, o nome da aba no prontuário, o local (Subjetivo ou Objetivo) e as instruções para o paciente.
3. Ligue **Validar pelo profissional?** e **Coletar CPF no formulário?**.
4. Adicione as perguntas (texto, número, data, sim/não, lista suspensa, múltipla escolha) e salve.

### 2. Exigir o formulário no procedimento

1. Acesse **Configurações › Procedimentos** e edite (ou crie) o procedimento.
2. Ligue **Exigir preenchimento de formulário no agendamento online**.
3. Em **Formulário exigido**, escolha o formulário.
4. Confira modalidade, valor e **profissionais executores**. Sem executor, o procedimento não aparece na Agenda Online.
5. Salve.

### 3. Liberar o formulário no prontuário

1. Acesse **Configurações › Configurar SOAP**.
2. Selecione o formulário e os profissionais ou especialidades que terão acesso a ele.
3. Salve.

## Como fica para o paciente e para o profissional

- **Paciente:** escolhe profissional, procedimento e horário. Antes de confirmar, aparece o formulário. Ele não consegue concluir o agendamento sem responder.
- **Profissional:** ao clicar em **Atender**, recebe o aviso de que há um formulário a validar. Ele abre, confere as respostas e salva. O formulário fica registrado no prontuário e na folha de rosto do paciente, com a data da resposta e quem validou.

## Regras importantes

- Cada procedimento aceita um formulário exigido.
- Só aparecem para escolha os formulários com **Coletar CPF no formulário?** ligado.
- Um formulário que está exigido em algum procedimento não pode ser inativado, excluído nem ter a coleta de CPF desligada. O sistema informa em quais procedimentos ele está. Remova a associação antes de alterar.
- A exigência vale para o agendamento feito pelo paciente na Agenda Online.

## Perguntas frequentes

- **O formulário não aparece na lista do procedimento.** Ligue **Coletar CPF no formulário?** no formulário.
- **Não vejo a opção de exigir formulário no procedimento.** O recurso depende do plano contratado. Fale com o suporte pelo botão **Falar com o suporte** na Central de Ajuda.
- **O profissional não vê o formulário no atendimento.** Confira se ele foi liberado em **Configurar SOAP**.
