import random
a1 = str(input('Digite o nome do 1º aluno(a): '))
a2 = str(input('Digite o nome do 2º aluno(a): '))
a3 = str(input('Digite o nome do 3º aluno(a): '))
a4 = str(input('Digite o nome do 4º aluno(a): '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno sortiado foi {}'.format(escolhido))