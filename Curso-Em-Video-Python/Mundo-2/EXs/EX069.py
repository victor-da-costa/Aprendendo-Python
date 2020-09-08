cont = Tidade = Thomens = Tmulheres = 0
while True:
    idade = int(input('Informe a sua idade: '))
    if idade > 18:
        Tidade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        Thomens += 1
    if idade < 20 and sexo == 'F':
        Tmulheres += 1
    cont += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'''Foram geristradas um total de {cont} pessoas, sendo {Tidade} delas tem mais de 
18 anos, dos {cont}, {Thomens} Homens e {Tmulheres} Mulheres com menos de 20 anos''')
