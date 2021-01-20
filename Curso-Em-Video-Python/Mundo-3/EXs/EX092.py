from datetime import datetime
dados = {}


dados['Nome'] = (str(input('Nome: ')))
nasc = int(input('Data de nascimento: '))
dados['Idade'] = (datetime.now().year - nasc)
dados['CTPS'] = (int(input('N° da carteira de trabalho: ')))
if dados['CTPS'] != 0:
    dados['Contratação'] = (int(input('Ano de Contratação: ')))
    dados['Salário'] = (int(input('Informe seu salário: ')))
    dados['Aposentadoria'] = (dados['Idade']) + ((dados['Contratação'] + 35) - datetime.now().year)

for key, valor in dados.items():
    print(f'{key}: {valor}')
