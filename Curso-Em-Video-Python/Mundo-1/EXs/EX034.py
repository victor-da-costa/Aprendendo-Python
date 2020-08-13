salário = int(input('Qual é o seu salário? '))
if salário > 1250:
    aumento = salário + (salário * 0.1)
if salário <= 1250:
    aumento = salário + (salário * 0.15)
print('O salário de R${} com o reajustado fica em R${:.2f}'.format(salário, aumento))