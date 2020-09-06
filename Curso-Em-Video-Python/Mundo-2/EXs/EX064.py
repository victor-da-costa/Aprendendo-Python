num = 0
cont = 0
soma = 0
num = int(input('Informe um número: [999 para parar] '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Informe um número: [999 para parar] '))
print('Você digitou {} números e a soma entre eles é de {}'.format(cont, soma))
