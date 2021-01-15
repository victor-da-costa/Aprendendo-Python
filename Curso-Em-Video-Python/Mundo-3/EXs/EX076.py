materiais = ('Caderno', 15.90, 'Mochila', 100, 'Livro', 35)

for iten in range(0, len(materiais)):
    if iten % 2 == 0:
        print(f'{materiais[iten]:.<25}', end='')
    else:
        print(f'R${materiais[iten]:<.2f}')
