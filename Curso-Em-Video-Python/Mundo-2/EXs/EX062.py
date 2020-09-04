termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termos = int(input('Quantos termos? ')) 
tot = 0
cont = 0
while termos != 0:
    tot += termos
    while cont < tot:
        print('{} >> '.format(termo), end='')
        cont += 1
        termo += razão
    print('PAUSA')
    termos = int(input('Quer mais quantos termos? '))
print('A progressão foi finalizado com {} termos'.format(tot))