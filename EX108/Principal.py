import moeda

valor = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Com um aumento de 10% o valor {moeda.moeda(valor)} fica igual a {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Com uma redução de 10% o valor {moeda.moeda(valor)} fica igual a {moeda.moeda(moeda.diminuir(valor, 10))}')
