termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 0
while cont < 10:
    print('{}'.format(termo), end='')
    print(' >> ' if cont < 9 else '', end='')
    cont += 1
    termo += razão
