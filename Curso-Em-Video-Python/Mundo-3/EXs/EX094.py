pessoas = []
individuo = {}
idade = 0
while True:
    individuo.clear()
    individuo['nome'] = str(input('Nome: ')).strip()
    while True:
        individuo['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if individuo['sexo'] in 'MF':
            break
        print('ERRO, Digite apenas [M] - Masculino ou [F] - Feminino')
    individuo['idade'] = int(input('Idade: '))
    idade += individuo['idade']
    pessoas.append(individuo.copy())
    while True:
        opção = str(input('Quer cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
        if opção in 'SN':
            break
        print('ERRO, Digite apenas [S] - Sim ou [N] - Não')
    if opção == 'N':
        break
print('='*35)
print(f'Foram cadastradas {len(pessoas)} pessoas na lista')
print(f'A médias da IDADE das pessoas cadastradas é {idade / len(pessoas):.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for mulher in pessoas:
    if mulher['sexo'] == 'F':
        print(f'{mulher["nome"]} ', end='')
print()
print(f'As pessoas cadastradas com idade acima de {idade / len(pessoas):.2f} são: ', end='')
for acima in pessoas:
    if acima['idade'] > idade / len(pessoas):
        print(f'{acima["nome"]} ', end='')
print()
