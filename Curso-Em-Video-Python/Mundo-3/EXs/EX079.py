numeros = []
while True:
    num = int(input('Digite um número: '))
    if num in numeros:
        print(f'O número {num} já existe na lista, portanto não será adicionado')
    else:
        numeros.append(num)
    continuar = str(input('Quer adicionar mais um número na lista? S/N ')).upper()
    if continuar == 'N':
        break

numeros.sort()
print(f'Os números adicionado a lista foram: {numeros}')
