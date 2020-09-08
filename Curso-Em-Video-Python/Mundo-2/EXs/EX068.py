from random import randint
#cont = 0
#while True:
#    num = int(input('Digite um valor: '))
#    while player not in 'PI'
#        player = str(input('PAR ou IMPAR: ')).strip().upper()[0]
#    computador = randint(0, 10)
#    soma = num + computador
#    if soma % 2 == 0 and player == 'P':
#        cont += 1
#        print(f'VOCÊ VENCEU!!! Você jogou {num} e o computador jogou {computador}')
#    if soma % 2 == 0 and player == 'I':
#        print(f'VOCÊ PERDEU!!! Você jogou {num} e o computador jogou {computador}')
#        break
#    if soma % 3 == 0 and player == 'I':
#        cont += 1
#        print(f'VOCÊ VENCEU!!! Você jogou {num} e o computador jogou {computador}')
#    if soma % 3 == 0 and player == 'P':
#        print(f'VOCÊ PERDEU!!! Você jogou {num} e o computador jogou {computador}')
#        break
#if cont == 1:
#    print(f'Você vendeu {cont} vez')
#else:
#    print(f'Você venceu {cont} jogos consecutivos')



cont = 0
while True:
    num = int(input('Digite um valor: '))
    player = str(input('PAR ou IMPAR: ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = num + computador
    if soma % 2 == 0:
        if player == 'P':
            cont += 1
            print(f'VOCÊ VENCEU!!! Você jogou {num} e o computador jogou {computador}')
        elif player == 'I':
            print(f'VOCÊ PERDEU!!! Você jogou {num} e o computador jogou {computador}')
            break
    if soma % 2 == 1:
        if player == 'I':
            cont += 1
            print(f'VOCÊ VENCEU!!! Você jogou {num} e o computador jogou {computador}')
        elif player == 'P':
            print(f'VOCÊ PERDEU!!! Você jogou {num} e o computador jogou {computador}')
            break
if cont == 1:
    print(f'Você vendeu {cont} vez')
else:
    print(f'Você venceu {cont} jogos consecutivos')