numeros = []
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print('Número duplicado...')
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(sorted(numeros))
