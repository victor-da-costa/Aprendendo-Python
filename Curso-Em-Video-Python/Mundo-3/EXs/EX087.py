pares = 0
col = 0
lin = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = (int(input('Digite o número: ')))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if matriz[linha][2]:
            col += matriz[linha][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
for coluna in range(0, 3):
    if coluna == 0:
        lin = matriz[1][coluna]
    elif:
        if matriz[1][coluna] > lin:
            lin = matriz[1][coluna]
print(f'A soma dos pares é {pares}')
print(f'A soma da terceira coluna é {col}')
print(f'O maior número da segunda linha é {lin}')
