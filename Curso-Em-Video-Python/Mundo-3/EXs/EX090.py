aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'REPROVADO'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'EM EXAME'
else:
    aluno['Situação'] = 'APROVADO'
print(f'{aluno["nome"]} está com média {aluno["Média"]}, e está: {aluno["Situação"]}')