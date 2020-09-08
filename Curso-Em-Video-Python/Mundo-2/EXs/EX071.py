valor = int(input('Quanto você quer sacar: R$'))
cédula = 50
tot = 0
while True:
    if valor >= cédula:
        valor -= cédula
        tot += 1
    else:
        if tot > 0:
            print(f'Total de {tot} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        tot = 0
        if valor == 0:
            break
