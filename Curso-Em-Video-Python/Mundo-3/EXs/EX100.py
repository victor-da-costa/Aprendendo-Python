from random import randint


def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(0, 10))
    print(numeros)


def somaPar(lista):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(soma)


numeros = []

sorteia(numeros)
somaPar(numeros)
