from random import randint

jogos = []
aposta = []

quant = int(input('Gerar quantos jogos? '))
while len(jogos) != quant:
    while True:
        num = randint(1, 60)
        if num not in aposta:
            aposta.append(num)
        if len(aposta) == 6:
            break
    jogos.append(aposta[:])
    aposta.clear()

print(jogos)
