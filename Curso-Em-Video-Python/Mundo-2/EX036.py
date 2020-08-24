valor = float(input('Qual é o valor do imóvel? R$ '))
salário = float(input('Qual é o valor do seu salário? R$ '))
prazo = int(input('Em quantos anos quer quitar o empréstimo? '))
prestação = valor/(prazo * 12)
if prestação > salário * 0.3:
    print('Empréstimo negado')
else:
    print('Empréstimo concedido, o emprestimo de R${} no prazo de {} anos tera uma prestação de {:.2f}'.format(valor, prazo, prestação))