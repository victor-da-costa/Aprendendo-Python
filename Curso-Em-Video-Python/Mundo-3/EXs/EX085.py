valores = [[], []]
for num in range(1, 8):
    número = (int(input(f'Digite o {num}º número: ')))
    if número % 2 == 0:
        valores[0].append(número)
    else:
        valores[1].append(número)
valores[0].sort()
valores[1].sort()
print(f'Lista de números pares: {valores[0]}')
print(f'Lista de números impares: {valores[1]}')
