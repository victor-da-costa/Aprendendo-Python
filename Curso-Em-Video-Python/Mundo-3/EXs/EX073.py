times = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 
'Ceará', 'Corinthians', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', 'Goiás', 'Botafogo', 'Coritiba')

print(f"Os 5 primeiros: {times[0:5]}")
print(f"Os 4 últimos {times[-4:]}")
print(f"Em ordem alfabética {sorted(times)}")
print(f"O Fluminense está na {times.index('Fluminense')+1}° posição")
