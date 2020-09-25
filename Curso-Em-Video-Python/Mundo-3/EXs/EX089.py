estudantes = []
while True:
    nome = str(input('Nome: '))
    nota01 = float(input('Nota 01: '))
    nota02 = float(input('Nota 02: '))
    média = (nota01 + nota02) / 2
    estudantes.append([nome, [nota01, nota02], média])
    opção = str(input('Quer continuar? ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'{"Num":<2} {"Nome":<10}{"Média":>2}')
for indice, aluno in enumerate(estudantes):
    print(f'{indice:<2}   {aluno[0]:<10}{aluno[2]:>2}')
while True:
    notas = int(input('Quer ver as notas de qual aluno(a)? (Obs: 999 para sair do programa) '))
    if notas == 999:
        break
    if notas <= len(estudantes) - 1:
        print(estudantes[notas][1])
