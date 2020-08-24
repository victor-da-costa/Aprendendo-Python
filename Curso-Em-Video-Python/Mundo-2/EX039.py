from datetime import date
ano = int(input('Em que ano você nasceu: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print('Você precisa se apresentar daqui a {} anos'.format(18 - idade))
elif idade == 18:
    print('Você deve se apresentar imediatamente!')
elif idade > 18:
    print('Você deveria ter se apresentado há {} anos'.format(idade - 18))
