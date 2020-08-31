from time import sleep
num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))
opção = 0
while opção != 5:
    print('''
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA
        ''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma dos números {} e {} é {}'.format(num1, num2, soma))
    elif opção == 2:
        mult = num1 * num2
        print('O resultado da multiplicação dos números {} e {} é {}'.format(num1, num2, mult))
    elif opção == 3:
        if num1 > num2:
            print('{} > {}'.format(num1, num2))
        else:
            print('{} > {}'.format(num2, num1))
    elif opção == 4:
        num1 = int(input('Informe o 1º número: '))
        num2 = int(input('Informe o 2º número: '))
    elif opção == 5:
        print('FINALIZANDO...')
        sleep(1)
        print('FIM DO PROGRAMA')
    else:
        print('OPÇÃO INVÁLIDA')