# Consegui fazer o exercicíos sem olhar a resposta.

from random import randint
print('='*75)
print('Estou pensando em um número ente 0 - 5...tente adivinhar qual é!')
print('='*75)
pc = randint(0, 5)
num = int(input('Digite um número: '))
if num == pc:
    print('PARABÉNS, você acertou!!!')
else:
    print('Você errou...')