palavras = ('Mercado', 'Programacao', 'Futuro', 'praticar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letras in p:
        if letras in 'aeiou':
            print(letras, end=' ')
