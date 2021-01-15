dados = []
alunos = []


while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('1° Nota: ')))
    dados.append(int(input('2° Nota: ')))
    dados.append((dados[1] + dados[2]) / 2)
    alunos.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar? S/N ')).upper()
    if continuar == 'N':
        break

print('Indice      Alunos      Nota 1   Nota 2   Média')
for indice, aluno in enumerate(alunos):
    print(f'{indice:<3} {aluno[0]:>11} {aluno[1]:>11} {aluno[2]:>8} {aluno[3]:>8}')