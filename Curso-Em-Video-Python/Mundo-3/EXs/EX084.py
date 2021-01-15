grupo = []
individuo = []

maior = menor = 0
while True:
    individuo.append(str(input('Nome: ')))
    individuo.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = individuo[1]
    else:
        if individuo[1] > maior:
            maior = individuo[1]
        if individuo[1] < menor:
            menor = individuo[1]
    grupo.append(individuo[:])
    individuo.clear()
    cont = str(input('Quer continuar? S/N ')).upper()
    if cont == 'N':
        break
print(grupo)
print(f'Foram cadastradas na lista {len(grupo)} pessoas')
print(f'A pessoa mais pesada da lista é {maior}')
print(f'A pessoa mais leve da lista é {menor}')
