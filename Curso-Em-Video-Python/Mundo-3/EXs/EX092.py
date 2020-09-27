from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
dados['nasc'] = int(input('Data de nascimento: '))
dados['carteira'] = int(input('Nº da Carteira de Trabalho: '))
if dados['carteira'] != 0:
    dados['idade'] = datetime.now().year - dados['nasc']
    dados['ano_contratação'] = int(input('Ano de Contratação: '))
    dados['aposentar'] = dados['idade'] + ((dados['ano_contratação'] + 35) - datetime.now().year)
    dados['salario'] = float(input('Salário: '))
print('=' * 30)
for indece, info in dados.items():
    print(f'{indece}: {info}')
