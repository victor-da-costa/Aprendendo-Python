from random import randint
lista = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
eu = int(input('''Escolha uma opção
[0] Pedra
[1] Papel
[2] Tesoura
Sua opção: '''))
if pc == 0:
    if eu == 0:
        print('EMPATE')
    elif eu == 1:
        print('JOGADOR GANHOU')
    elif eu == 2:
        print('COMPUTADOR GANHOU')

elif pc == 1:
    if eu == 0:
        print('COMPUTADOR GANHOU')
    elif eu == 1:
        print('EMPATE')
    elif eu == 2:
        print('JOGADOR GANHOU')

elif pc == 2:
    if eu == 0:
        print('JOGADOR GANHOU')
    elif eu == 1:
        print('COMPUTADOR GANHOU')
    elif eu == 2:
        print('EMPATE')
print('='*22)
print('Jogador jogou {}'.format(lista[eu]))
print('Computador jogou {}'.format(lista[pc]))
print('='*22)
