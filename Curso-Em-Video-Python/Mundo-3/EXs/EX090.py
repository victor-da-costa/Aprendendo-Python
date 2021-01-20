dados = {}

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))
if dados['media'] >= 7:
    dados['situacao'] = ('Aprovado(a)')
elif dados['media'] >= 5:
    dados['situacao'] = ('Exame')
else:
    dados['situacao'] = ('Reprovado')

for k, v in dados.items():
    print(f'{k} é igual a {v}')
