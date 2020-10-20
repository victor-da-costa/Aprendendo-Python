def leiaint(txt):
    ok = False
    valor = 0
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            ok = True
            valor = int(num)
        else:
            print('ERRO! Digite um número inteiro')
        if ok == True:
            break
    return valor


num = leiaint('Digite um número: ')
print(f'Você digitou o número {num}')
