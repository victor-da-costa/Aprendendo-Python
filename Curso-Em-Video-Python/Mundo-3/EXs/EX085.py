numeros = [[], []]

for n in range(0, 7):
    num = int(input(f'Digite o {n+1}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
    
    print(f'Números adicionados à lista: {numeros}')
    print(f'Números pares adicionados à lista: {numeros[0]}')
    print(f'Números impares adicionados à lista: {numeros[1]}')
