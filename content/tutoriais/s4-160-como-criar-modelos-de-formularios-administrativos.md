---
titulo: Como criar modelos de formulários administrativos
slug: como-criar-modelos-de-formularios-administrativos
secao: configuracoes-do-gestor
ordem: 160
perfis: Administrador da conta, Administrador da clínica, Recepção
caminho: Configurações › Modelos › Formulários
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Modelos de formulários administrativos são documentos da recepção que saem já preenchidos com os dados do paciente e do profissional: termo de consentimento presencial, contrato de prestação de serviço, declaração de comparecimento, recibo, ficha de pré-consulta. A equipe cria o modelo uma vez e imprime pelo agendamento sempre que precisar.

## Quem pode fazer

- Criar e editar modelos: gestores (Admin de Conta e Admin de Clínica).
- Imprimir pelo agendamento: quem tem acesso à agenda, como a recepção.

## Onde fica

**Configurações › Modelos › Formulários**

## Antes de começar

- Configure os impressos da clínica (logo, nome, endereço e telefone). Os formulários saem com esse mesmo cabeçalho e rodapé.

## Passo a passo

1. Acesse **Configurações › Modelos › Formulários** e clique em **Adicionar**.
2. Preencha o **Título** (obrigatório), por exemplo "Declaração de comparecimento" ou "Recibo".
3. No campo **Modelo**, escreva o texto. O editor funciona como um editor de textos comum: negrito, tamanho de fonte, alinhamento, listas, tabelas e caixas de marcação.
4. Insira os dados dinâmicos onde quiser que o sistema preencha sozinho, como nome completo, data de nascimento, idade, CPF, data atual e nome e registro do profissional.
5. Deixe em branco os trechos que serão completados na hora (por exemplo, valor ou dias de afastamento).
6. Clique em **Salvar**.

Use **Editar** para ajustar um modelo e **Remover** para excluí-lo (o sistema pede confirmação).

## Como imprimir um formulário

1. Na **Agenda** (ou pela **Sala de Espera**), abra o agendamento do paciente.
2. Clique em **Mais ações › Imprimir formulário**.
3. Em **Modelos de formulário**, escolha o modelo. O texto aparece com os dados do paciente, do profissional e do agendamento já preenchidos.
4. Complete o que faltar e clique para imprimir.

Funciona também em encaixes.

## Regras importantes

- Formulário administrativo é diferente de **Formulários personalizados**: estes são questionários e instrumentos que aparecem dentro do prontuário (SOAP). Os administrativos são documentos para imprimir e entregar.
- O cabeçalho do documento impresso vem sempre da configuração de impressos da clínica. Para mudar logo ou nome, altere lá, não no modelo.
- Os dados dinâmicos usam o que está no cadastro. Se o CPF ou a data de nascimento estiverem vazios, o campo sai em branco.
- Os modelos ficam disponíveis para toda a clínica.

## Perguntas frequentes

- **Quero que a ficha saia com o logo e o nome da unidade. Como faço?** Configure os impressos da clínica; o formulário usa esse cabeçalho.
- **Consigo transformar um PDF que a clínica já usa em modelo?** Sim, copie o texto para o editor e substitua os dados do paciente pelos dados dinâmicos. Layouts muito específicos podem não ficar idênticos ao PDF.
- **O paciente consegue preencher o formulário pela internet?** Não, este recurso é para impressão. Para o paciente responder online, use os formulários personalizados.
