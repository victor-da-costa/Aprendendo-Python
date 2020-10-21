import moeda

valor = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Com um aumento de 10% o valor {moeda.moeda(valor)} fica igual a {moeda.aumentar(valor, 10, True)}')
print(f'Com uma redução de 10% o valor {moeda.moeda(valor)} fica igual a {moeda.diminuir(valor, 10, True)}')
