valor = float(input('Valor em compras? R$ '))
opção = int(input('''Formas de pagamento: 
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão

Esconha um opção: '''))
if opção == 1:
    pagar = valor - (valor * 0.1)
    print('Compras pagas à vista em dinheiro e cheque tem 10% de desconto, e fica por R${:.2f}'.format(pagar))
elif opção == 2:
    pagar = valor - (valor * 0.05)
    print('Compras pagas à vista no cartão tem 5% de desconto, e fica por R${:.2f}'.format(pagar))
elif opção == 3:
    parcelar = int(input('Quer parcelar em quantas vezes? '))
    pagar = valor / parcelar
    print('Você optou em parcelar em {}x de R${:.2f}'.format(parcelar, pagar))
elif opção == 4:
    parcelar = int(input('Quer parcelar em quantas vezes? '))
    pagar = (valor * 1.2) / parcelar
    print('Você optou em parcelar em {}x de R${:.2f}'.format(parcelar, pagar))
else:
    print('Opção invalida, escolha uma das opções acima!')

