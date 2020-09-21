matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[coluna].append(int(input('Digite o número: ')))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
