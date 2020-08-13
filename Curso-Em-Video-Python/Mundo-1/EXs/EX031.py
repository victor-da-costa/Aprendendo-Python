# Consegui fazer o exercicíos sem olhar a resposta.

km = int(input('Qual a distância de sua viagem: '))
if km < 200:
    custo1 = km * 0.5
    print('O custo para fazer uma viagem de {}Km é de R${:.2f}'.format(km, custo1))
else:
    custo2 = km * 0.45
    print('O custo para fazer uma viagem de {}Km é de R${:.2f}'.format(km, custo2))


# Maneira simplificada...
#
# km = int(input('Qual a distância de sua viagem: '))
# if km <= 200: custo = km * 0.5 else custo = km * 0.45
#   print('O custo para fazer uma viagem de {}Km é de R${:.2f}'.format(km, custo))
