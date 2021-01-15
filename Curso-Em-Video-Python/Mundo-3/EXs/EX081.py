numeros = []

while True:
    numeros.append(int(input('Informe um número: ')))
    cont = str(input('Quer continuar? S/N ')).upper()
    if cont == 'N':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números')
print(f'Lista em ordem decrescente: {numeros}')
if 5 in numeros:
    print('O número 5 está na lista')
else:
    print('O número 5 não foi encontrado na lista')
