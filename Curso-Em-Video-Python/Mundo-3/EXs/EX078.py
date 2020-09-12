lista = []
maior = 0
menor = 0
for num in range(0, 5):
    lista.append(int(input(f'Digite o {num + 1}º da lista: ')))
    if num == 0:
        maior = lista[num]
        menor = lista[num]
    else:
        if lista[num] > maior:
            maior = lista[num]
        if lista[num] < menor:
            menor = lista[num]
print(f'O maior e menor número da lista é {maior} e {menor} que estão nas posição', end=' ')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(pos, end=' ')
for pos, valor in enumerate(lista):
    if valor == menor:
        print(pos, end=' respectivamente...')
