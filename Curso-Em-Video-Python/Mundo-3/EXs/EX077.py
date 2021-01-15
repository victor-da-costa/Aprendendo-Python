palavras = ('aprender', 'programar', 'python')

for iten in palavras:
    print(f'\nNa palavra {iten} temos: ', end='')
    for letra in iten:
        if letra in 'aeiou':
            print(f'{letra} ', end='')
