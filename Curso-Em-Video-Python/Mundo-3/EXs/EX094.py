grupo = []
pessoa = {}

soma_idades = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        resposta = str(input('Quer Continuar? S/N ')).upper()[0]
        if resposta in 'SN':
            break
    grupo.append(pessoa.copy())
    if resposta == 'N':
        break

print(f'A) Foram registadas {len(grupo)} pessoas na lista')
média = soma_idades / len(grupo)
print(f'B) A média de idade das pessoas registradas é {média} anos')
print('C) Lista das Mulheres cadastradas: ', end='')
for P in grupo:
    if P['Sexo'] == 'F':
        print(f'{P["Nome"]}', end='')
print()
print('D) Lista das pessoas que tem idade maior que a média')
for P in grupo:
    if P['Idade'] > média:
        for k, v in P.items():
            print(f'{k} tem {v}; ', end='')
        print()
   