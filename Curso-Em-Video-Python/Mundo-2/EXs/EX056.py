tot = 0
Nhomem = ''
Ihomem = 0
mulher = 0
for pessoa in range(1, 5):
    nome = str(input('Qual é o nome da {}º pessoa? '.format(pessoa))).strip().upper()
    idade = int(input('Qual é a idade dessa pessoa? '))
    sexo = str(input('Qual é o sexo? [M/F] ')).strip().upper()
    tot += idade
    média = tot / pessoa
    if pessoa == 1 and sexo == 'M':
        Nhomem = nome
        Ihomem = idade
    if idade > Ihomem and sexo == 'M':
        Nhomem = nome
        Ihomem = idade
    if idade < 20 and sexo == 'F':
        mulher += 1
print('''A média de idade do grupo é de {} anos
O homem mais velho do grupo tem {} anos e se chama {}
E {} mulher tem menos de 20 anos'''.format(média, Ihomem, Nhomem, mulher))