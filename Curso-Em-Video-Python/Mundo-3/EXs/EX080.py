numeros = []
for num in range(0, 5):
    n = int(input(f'Digite o {num+1}° número: '))
    if num == 0 or n > numeros[-1]:
        numeros.append(n)
pos = 0
while n < len(numeros):
    if pos <= numeros[pos]:
        numeros.insert(pos, n)
        break
    pos += 1
print(numeros)
