def ficha(jogador='<desconhecido>', num=0):
    print(f'O jogador {nome} fez {gols} gol(s) na temporada.')


nome = str(input('Nome do jogador: '))
gols = str(input('Nº de gol(s): '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols)
else:
    ficha(nome, gols)
