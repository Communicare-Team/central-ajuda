---
titulo: Como lançar um recebimento
slug: como-lancar-um-recebimento
secao: financeiro-e-faturamento
ordem: 60
perfis: Recepção, Administrador da clínica, Administrador da conta
caminho: 
video: 
video_rotulo: 
atualizado: 2026-11-01
---
## Para que serve

Lançar o recebimento registra que o paciente pagou a consulta, como pagou e quando. É isso que alimenta o extrato, o relatório financeiro, o repasse dos profissionais e a nota fiscal automática. Mesmo que o paciente tenha pago por fora (Pix direto, dinheiro), o recebimento precisa ser lançado para os números da clínica ficarem corretos.

## Quem pode fazer

Recepcionista Administrativo, Admin de Clínica, Admin de Conta e demais usuários com acesso à agenda. Usuários marcados como restritos não abrem a tela de recebimento.

## Onde fica

- **Sala de espera**: ícone de cifrão (**Lançar recebimento**) no card do paciente.
- **Agenda**: clique no agendamento e depois em **Receber pagamento**. Na visualização em lista, use **Receber**.
- **Sala multi**: ícone de cifrão no card.

## Antes de começar

- O agendamento precisa estar salvo.
- As formas de recebimento devem estar cadastradas em **Financeiro › Receitas e despesas › Formas de recebimento**.

## Passo a passo

1. Abra o recebimento por um dos caminhos acima. A tela já traz o serviço agendado e o valor.
2. Se houver desconto, informe em **Desconto**. O valor a receber diminui.
3. Se o paciente fez outro procedimento ou exame na consulta, inclua em **Procedimentos Associados**. O total é atualizado.
4. Escolha a **Forma de pagamento**. O valor vem preenchido.
5. Confira a **Data do recebimento** (vem a de hoje; altere para a data em que o dinheiro foi realmente recebido).
6. Se foi no crédito parcelado, ligue **Parcelar** e escolha o número de **Parcelas**.
7. Deixe **Recebido** ligado.
8. Se o paciente pagou em duas formas (parte em Pix, parte no cartão), clique em **Adicionar recebimento** e lance a segunda forma até o **Saldo restante** ficar zerado.
9. Clique em **Confirmar recebimento** e salve.

Depois de salvo, o agendamento passa a **Recebido** e mostra o cifrão na agenda. Pela mesma tela você pode emitir o **Recibo** e, se a clínica emite notas, a **Nota fiscal**.

## Regras importantes

- Status possíveis: **A receber**, **Recebimento parcial** e **Recebido**.
- O desconto não pode ser maior que o valor do agendamento.
- Se o paciente pagou pelo link de pagamento online ou pela Agenda Online, a baixa é automática. Não lance de novo.
- O link de pagamento (**Compartilhar link de pagamento**) só aparece se o pagamento online estiver configurado e o status for **A receber**.
- Com recebimento lançado, o convênio e o procedimento do agendamento ficam travados. Para trocar, desfaça o recebimento antes.
- O repasse ao profissional só é calculado com o recebimento lançado (exceto convênio com TISS).
- Para a nota fiscal sair automaticamente, o recebimento precisa estar lançado integralmente antes de finalizar o atendimento.
- Atendimentos pagos com crédito de pacote ficam como **Recebido** automaticamente.

## Perguntas frequentes

- **Lancei errado. Como corrijo?** Abra o agendamento e use **Editar pagamento** ou **Desfazer recebimento**.
- **O paciente pagou só uma parte.** Lance o valor recebido; o status fica **Recebimento parcial** e o saldo restante aparece. Quando ele pagar o restante, use **Editar pagamento** e adicione o novo recebimento.
- **Não consigo trocar o procedimento do agendamento.** Já existe recebimento lançado. Desfaça o recebimento, ajuste e lance de novo.
- **Como devolvo um pagamento online?** O estorno é feito pelo Admin de Conta no próprio agendamento. Veja o tutorial de estornos.
