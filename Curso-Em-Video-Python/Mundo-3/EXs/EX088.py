from random import randint
jogos = []
numeros = []
palpites = int(input('Gerar quantos jogos? '))
for cont in range(0, palpites):
    while True:
        num = randint(1, 61)
        if num not in numeros:
            numeros.append(num)
            if len(numeros) == 6:
                break
    jogos.append(numeros[:])
    numeros.clear()
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice}: {lista}')
