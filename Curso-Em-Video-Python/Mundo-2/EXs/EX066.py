cont = soma = 0
while True:
    num = int(input('Digite um valor: [999 para parar o programa] '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram informados {cont} números, no qual a soma é de {soma}')