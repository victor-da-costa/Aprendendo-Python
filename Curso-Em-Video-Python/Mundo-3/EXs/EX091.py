from random import randint
from operator import itemgetter
resultados = {'P01': randint(1, 6),
              'P02': randint(1, 6),
              'P03': randint(1, 6),
              'P04': randint(1, 6)}
for player, resul in resultados.items():
    print(f'{player} tirou {resul}')
print('='*25)
ranking = {}
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('  == RANKING ==  ')
for indice, pos in enumerate(ranking):
    print(f'   {indice + 1}º lugar: {pos[1]}')
