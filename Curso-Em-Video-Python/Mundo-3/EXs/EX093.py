dados = {}
partidas = []

dados['Nome'] = str(input('Nome: '))
total = int(input('N° de partidas jogadas: '))
for jogo in range(0, total):
    partidas.append(int(input(f'Quantos gols feitos na {jogo}° partida: ')))
dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)
print('=' * 25)
for key, valor in dados.items():
    print(f'O campo {key} tem o valor {valor}')
print('=' * 25)
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas')
print('=' * 25)
for indice, valor in enumerate(dados['Gols']):
    print(f'  >> Na partida {indice}, fez {valor} gols')
print('=' * 25)
