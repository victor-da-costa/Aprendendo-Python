materiais = ('Caderno', '15.9', 'Borracha', '2', 'Lápis', '1.75', 'Estojo', '25', 'Compasso', '9.99')
for m in range(len(materiais)):
    if m % 2 == 0:
        print(f'{materiais[m]:.<30}', end='')
    else:
        print(f'R${materiais[m]}')
