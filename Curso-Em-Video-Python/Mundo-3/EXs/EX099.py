def maior(*num):
    cont = maior = 0
    for número in num:
        print(f'{número}', end=' ')
        if cont == 0:
            maior = número
        else:
            if número > maior:
                maior = número
        cont +=1
    print(f'o maior número é o {maior}')
maior(1, 5, 6, 95, 30, 25)
