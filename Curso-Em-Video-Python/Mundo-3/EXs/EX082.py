'''
par = []
impar = []
numeros = []


while True:
    num = int(input('Informe um número: '))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    cont = str(input('Quer continuar? S/N ')).upper()
    if cont == 'N':
        break
print(f'A lista contem os números: {numeros}')
print(f'Os números pares contidos na lista: {par}')
print(f'Os números impares contidos na lista: {impar}')
'''

par = []
impar = []
numeros = []
while True:
    numeros.append(int(input('Informe um número: '))
    cont = str(input('Quer continuar? S/N ')).upper()
    if cont == 'N':
        break
for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'A lista contem os números: {numeros}')
print(f'Os números pares contidos na lista: {par}')
print(f'Os números impares contidos na lista: {impar}')
