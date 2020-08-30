from datetime import date
atual = date.today().year
maior = 0
menor = 0
for nasc in range(1, 8):
    ano = int(input('Em que ano a {}º nasceu? '.format(nasc)))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são de menor e {} são maiores de idade!'.format(menor, maior))