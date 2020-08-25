# Não é preciso verificar se a pessoa tem mais de 9 anos na linha 9 (por exemplo), se o programa
# Passou a linha 7, significa que a pessoa está na faixa de pelo menos 9-14 anos...

from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')