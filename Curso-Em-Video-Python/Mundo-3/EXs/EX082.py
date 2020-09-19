valores = []
impar = []
par = []
while True:
    num = int(input('Digite o valor: '))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'Os valores digitados são {valores}, a lista de números pares {par} e impar {impar}')
