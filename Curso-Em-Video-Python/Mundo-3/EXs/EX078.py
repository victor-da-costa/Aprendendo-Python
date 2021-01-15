numeros = []
for num in range(0, 5):
    numeros.append(int(input(f"Digite o {num+1}° número: ")))
    if num == 0:
        maior = menor = numeros[num]
    else:
        if numeros[num] > maior:
            maior = numeros[num]
        if numeros[num] < menor:
            menor = numeros[num]

print(f'O maior número da lista é o {maior}, e aparece na posição', end='')
for posicao, num in enumerate(numeros):
    if num == maior:
        print(f' {posicao}° ', end='')
print()
print(f'O menor número da lista é o {menor}, e aparece na posição', end='')
for posicao, num in enumerate(numeros):
    if num == menor:
        print(f' {posicao}° ', end='')
print()