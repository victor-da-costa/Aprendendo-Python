time = []
dados = {}
partidas = []


while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    total = int(input('N° de partidas jogadas: '))
    partidas.clear()
    for jogo in range(0, total):
        partidas.append(int(input(f'Quantos gols feitos na {jogo}° partida: ')))
    dados['Gols'] = partidas[:]
    dados['Total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resposta = str(input('Quer continuar? S/N ')).upper()[0]
            if resposta in 'SN':
                break
        if resposta == 'N':
            break
print('Código', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar os dados de qual jogador? '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'Não existe jogador com código {busca}')
    else:
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   >> No {i+1}° jogo fez {g} gols')
