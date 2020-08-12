dias = int(input('Por quantos dias o carro fico alugado? '))
km = float(input('Quantos Km você percorreu com o carro? '))
custo = (dias * 60) + (km * 0.15)
print('O custo por algar o carro por {} dias e percorrer {} Km foi de R${:.2f}'.format(dias, km, custo))