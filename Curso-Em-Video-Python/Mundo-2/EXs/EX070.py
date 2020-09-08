tot = mil = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: '))
    if preço > 1000:
        mil += 1
    tot += preço
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'''O total da compra deu R${tot:.2f}
{mil} produtos custaram mais de R$1000,00
O {barato} é o produto mais batato custando R${menor:.2f}''')
