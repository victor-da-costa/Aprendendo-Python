from random import randint
from operator import itemgetter

resultados = {
    'player01': randint(1, 6),
    'player02': randint(1, 6),
    'player03': randint(1, 6),
    'player04': randint(1, 6),
                }

ranking = {}
for k, v in resultados.items():
    print(f'{k} tirou {v}')
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

for ind, valor in enumerate(ranking):
    print(f'{ind}° lugar: {valor[0]} tirou {valor[1]}')
