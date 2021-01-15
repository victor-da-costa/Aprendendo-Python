matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_par = 0
maior_linha = 0
soma_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um número: '))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if matriz[1][c] > maior_linha:
            maior_linha = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for l in range(0, 3):
    soma_coluna += matriz[l][2]

print(soma_par)
print(soma_coluna)
print(maior_linha)
