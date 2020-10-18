from random import randint
def sorteia(lista):
    for cont in range(1, 6):
        num = randint(0, 10)
        numeros.append(num)
        print(f'{num} ', end='')
    print('PRONTO')

def soma_par(lista):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros} temos {soma}')


numeros = []
sorteia(numeros)
soma_par(numeros)
