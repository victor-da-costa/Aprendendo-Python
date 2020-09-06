soma = 0
cont = 0
opção = 'S'
while opção != 'N':
    num = int(input('Informe um número: '))
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Foram digitados {} números, a média entre eles é {}, o maior é {} e o menor é {}'.format(cont, media, maior, menor))