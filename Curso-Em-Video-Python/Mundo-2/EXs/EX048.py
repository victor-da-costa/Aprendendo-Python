soma = 0
cont = 0
for num in range (1, 501, 2):
    if num % 3 == 0:
        soma += num
        cont += 1
print('A soma dos {} números impar múltiplos de três é {}'.format(cont, soma))
