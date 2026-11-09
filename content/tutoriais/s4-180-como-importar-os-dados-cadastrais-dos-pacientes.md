---
titulo: Como importar os dados cadastrais dos pacientes
slug: como-importar-os-dados-cadastrais-dos-pacientes
secao: configuracoes-do-gestor
ordem: 180
perfis: Administrador da conta
caminho: Pacientes › Ações rápidas › Importar planilha
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

A importação por planilha cadastra muitos pacientes de uma vez, por exemplo ao começar a usar a Communicare ou ao receber a lista de um convênio. A mesma planilha também atualiza dados de pacientes já cadastrados e permite inativar pacientes em massa.

## Quem pode fazer

Dono da conta ou Admin de Conta. Outros perfis veem a mensagem "É necessário ser um admin de conta para importar pacientes".

## Onde fica

**Pacientes** › **Ações rápidas** (ícone de setas) › **Importar planilha**

## Antes de começar

- Use sempre o modelo da própria tela (**Baixar Template**). Ele tem uma aba de instruções com cada coluna, se é obrigatória, o formato e exemplos.
- Se for vincular pacientes a um convênio, cadastre o convênio antes e use exatamente o mesmo nome na planilha.

## Passo a passo

1. Acesse **Pacientes › Ações rápidas › Importar planilha**.
2. Clique em **Baixar Template** e preencha a planilha:
   - **nome** e **cpf** são obrigatórios (CPF com 11 dígitos);
   - os demais campos são opcionais: sexo, nascimento, celular, e-mail, endereço, convênio, entre outros;
   - siga o formato indicado nas instruções (datas e telefones sem pontos, traços, aspas ou colchetes);
   - mantenha a ordem das colunas e apague linhas e colunas vazias.
3. Volte à tela e clique em **Nova Importação**.
4. Dê um **Título da Importação** (mínimo 3 caracteres, por exemplo "Base inicial março") e selecione o arquivo. Clique em **Próximo**.
5. Confira o **Resumo da Importação** e o **Mapeamento de Colunas** (colunas aceitas e ignoradas).
6. Clique em **Importar**. A mensagem "Importação iniciada com sucesso!" confirma o início.
7. Acompanhe o andamento na lista de importações. Em **Ver detalhes**, veja todos os registros ou só os que deram erro.

## Regras importantes

- O CPF identifica o paciente: se ele já existe na conta, a importação atualiza o cadastro em vez de criar outro.
- Para inativar pacientes, preencha a coluna **ativado** com "não". Com "sim" (ou vazio), o paciente fica ativo.
- Cada planilha aceita até 35.000 linhas. Para bases maiores, divida em vários arquivos.
- Linhas vazias são ignoradas.
- A importação roda em segundo plano. Se for interrompida, use **Continuar importação** para retomar de onde parou.
- Erros de formato ou campo obrigatório vazio impedem a importação da linha; confira a lista de erros e corrija na planilha.
- Paciente importado não ganha login na Agenda Online. Para isso, ele se cadastra lá com o mesmo CPF.

## Perguntas frequentes

- **Importei e as datas de nascimento ficaram erradas (por exemplo, 2066 em vez de 1966). Por quê?** A data estava em formato diferente do template. Corrija na planilha e importe de novo; o CPF atualiza o cadastro.
- **Como incluo muitos pacientes em um convênio de uma vez?** Use a importação preenchendo a coluna de convênio com o nome exato do convênio.
- **Tenho pacientes sem CPF.** A importação exige CPF. Para bases sem CPF, fale com o suporte pelo botão **Falar com o suporte** na Central de Ajuda.
- **Dá para importar agendamentos ou prontuários de outro sistema?** Pela tela, não. Essa migração é feita pela equipe técnica; solicite pelo suporte.
