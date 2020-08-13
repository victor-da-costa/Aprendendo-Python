# Consegui fazer o exercicíos sem olhar a resposta.

velocidade = int(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    excedente = (velocidade - 80) * 7
    print('Você ultrapassou o limite de velocidade de 80Km/h e foi MULTADO em R${:.2f}'.format(excedente))
else:
    print('Tenha um bom dia! Dirija com segurança!')

# Modo simplificado...
#
# velocidade = int(input('Qual é a velocidade do carro? '))
# if velocidade > 80:
#     excedente = (velocidade - 80) * 7
#     print('Você ultrapassou o limite de velocidade de 80Km/h e foi MULTADO em R${:.2f}'.format(excedente))
# print('Tenha um bom dia! Dirija com segurança!')