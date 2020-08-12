salario = float(input('Quanto você ganha? R$'))
novo = salario + (salario*15/100)
print('O funcionario que antes ganhava R${:.2f} agora ganha {:.2f} após o aumento de 15%'.format(salario, novo))