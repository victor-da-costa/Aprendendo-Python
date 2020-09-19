valores = []
while True:
    valores.append(int(input('Digite o valor: ')))
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
valores.sort(reverse=True)
print(f'A lista {valores} contem {len(valores)} valores')
if 5 in valores:
    print('O número 5 foi encontrado na lista...')
else:
    print('O número 5 NÃO foi encontrado...')