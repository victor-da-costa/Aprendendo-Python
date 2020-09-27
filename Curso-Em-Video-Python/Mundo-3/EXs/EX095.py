time = []
gols = []
jogador = {}
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    jogador['jogos'] = int(input('Nº de partidas jogadas: '))
    gols.clear()
    for partidas in range(0, jogador['jogos']):
        num = int(input(f'Nº de gols na {partidas + 1}º '))
        gols.append(num)
    jogador['gols'] = gols[:]
    jogador['total_gols'] = sum(gols)
    time.append(jogador.copy())
    print(f'{"Nº"}  {"Nome"}         {"Partidas"}         {"Gols"}      {"Total de gols"}')
    for indice, valor in enumerate(time):
        print(f'{indice:>}', end='    ')
        for cont in valor.values():
            print(f'{str(cont):<15}', end='')
        print()
    while True:
        opção = str(input('Quer adicionar mais um jogador? [S/N] ').strip().upper()[0])
        if opção in 'SN':
            break
        print('ERRO! Tente novamente')
    if opção == 'N':
        break
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca > len(time):
        print('ERRO! Tente novamente')
    else:
        print(f' == LEVANTAMENTO DO {time[busca]["nome"]} ==')
        for k, v in enumerate(time[busca]['gols']):
            print(f' >> {k+1}º partida: {v}')
print('PROGRAMA FINALIZADO')
