from random import randint
cont = 0
print('Tente adivinhar em que número entre 0-10 estou pensando...')
computador = randint(0, 10)
player = int(input('Em que número o computador está pensando? '))
cont += 1
while computador != player:
    if computador > player:
        player = int(input('Mais...tente novamente '))
        cont += 1
    if computador < player:
        player = int(input('Menos, tente novamente '))
        cont += 1
print('Você acertou na {} tentaviva...PARABÉNS!!!'.format(cont))