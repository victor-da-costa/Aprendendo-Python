jogador = {}
gols = []
jogador['nome'] = str(input('Nome: '))
jogador['jogos'] = int(input('Nº de partidas jogadas: '))
for partidas in range(0, jogador['jogos']):
    num = int(input(f'Nº de gols na {partidas + 1}º '))
    gols.append(num)
jogador['gols'] = gols
jogador['total'] = sum(gols)
print(jogador)
print('='*30)
for indice, valor in jogador.items():
    print(f'{indice}: {valor}')
print('='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f' >> {i+1}º partida: {v}')
print(f'{jogador["nome"]} fez um total de {jogador["total"]} gols.')
