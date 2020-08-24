num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma base de conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
escolha = int(input('Converter para: '))
if escolha == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num) [2:]))
elif escolha == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Escolha invalida, tente novamente!')