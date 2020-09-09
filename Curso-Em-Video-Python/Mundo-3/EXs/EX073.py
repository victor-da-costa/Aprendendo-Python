times = ('Internacional', 'São Paulo', 'Atlético Mineiro', 'Vasco da Gama', 'Flamengo', 'Palmeiras', 
'Santos', 'Fluminense', 'Sport Recife', 'Ceará', 'Corinthians', 'Bahia', 'Fortaleza', 'Grêmio', 'Botafogo', 
'Athletico-PR', 'Coritiba', 'Atlético Goianiense', 'Bragantina', 'Goiás')

print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 ultimos colocados da tabela são: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O Fluminense está na {times.index("Fluminense")+1}ª posição da tabela')