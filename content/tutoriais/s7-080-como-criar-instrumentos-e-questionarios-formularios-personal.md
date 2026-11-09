---
titulo: Como criar instrumentos e questionários (formulários personalizados)
slug: como-criar-instrumentos-e-questionarios-formularios
secao: funcionalidades-avancadas
ordem: 80
perfis: Administrador da clínica, Administrador da conta
caminho: Configurações › Formulários personalizados
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Os formulários personalizados criam abas próprias no prontuário: questionários de pré-consulta, campos específicos da especialidade ou instrumentos com pontuação (escalas com score e classificação). O paciente pode responder por link antes da consulta e as respostas aparecem no prontuário.

## Quem pode fazer

Gestores (administrador da clínica ou da conta). Os profissionais preenchem e validam no atendimento.

## Onde fica

**Configurações › Formulários personalizados** (criar) e **Configurações › Configurar SOAP** (definir onde e para quem aparece).

## Antes de começar

- Recurso disponível conforme o plano contratado. Sem ele, a tela mostra um aviso para atualizar o plano.
- Para o paciente responder por link, ele precisa estar cadastrado com CPF.
- Para instrumentos com score, tenha em mãos o manual (pontuação de cada resposta e faixas de resultado).

## Passo a passo

1. Acesse **Configurações › Formulários personalizados** e clique em **Adicionar formulário**.
2. Preencha **Nome do formulário personalizado**, **Nome do formulário na aba do SOAP** (até 16 caracteres) e **Local do SOAP** (Subjetivo ou Objetivo).
3. Escreva as **Instruções** (o paciente vê ao abrir o link).
4. Ajuste as opções:
   - **Validar pelo profissional?**: ligado, a resposta do paciente só entra no prontuário depois que o profissional confere e salva.
   - **Coletar CPF no formulário?**: identifica o paciente. Desligado, o formulário fica anônimo.
   - **Coletar área e cargo?**: para pesquisas em empresas.
   - **Exibir como tabela no SOAP?**, **Dias para responder novamente** e **Ativar cálculo de score?**.
5. Clique em **Adicionar campo** e escolha o tipo: texto, número (unidade, mínimo, máximo, decimais), data, sim/não, lista suspensa, múltipla escolha ou caixas de marcar. Também é possível **Construir fórmula** com dois ou mais campos numéricos. Marque como obrigatório se necessário.
6. Com score ligado: crie os módulos, dê pontuação a cada opção e, em **Faixas de Resultado**, escolha soma ou média e cadastre as faixas de cada módulo.
7. Salve.
8. Em **Configurações › Configurar SOAP**, arraste o formulário para a posição desejada, marque as profissões e especialidades que vão vê-lo e clique em **Salvar**.

## Como enviar ao paciente

Na lista de formulários, use **compartilhar link** e envie pelo WhatsApp. Para enviar automaticamente, veja Como configurar o envio automático de formulários nas linhas de cuidado.

## Regras importantes

- Sem o passo em **Configurar SOAP**, o formulário não aparece para o profissional.
- As faixas de score não podem se sobrepor: o início de uma faixa não pode repetir o fim da anterior. Só salva com todos os módulos e faixas preenchidos.
- Formulário enviado ao paciente precisa estar salvo para finalizar o atendimento.
- Pacientes com cadastro inativo não conseguem responder.
- Use **duplicar** para criar versões e **inativar** em vez de apagar.

## Perguntas frequentes

- **Criei o formulário e o médico não vê.** Vincule a profissão/especialidade em **Configurar SOAP**.
- **O link não abre para o paciente.** Confirme se ele tem CPF no cadastro. Se persistir, peça para limpar o cache do navegador.
- **Dá erro ao salvar as faixas.** Confira se não há sobreposição e se todos os módulos têm faixas.
- **Posso corrigir um registro já salvo no atendimento?** Exclua o registro e preencha de novo.
