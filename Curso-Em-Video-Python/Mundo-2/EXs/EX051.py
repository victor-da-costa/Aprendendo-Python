# Não consegui fazer sem olha a resposta!

termo = int(input('Informe o primeiro termo da PA: '))
razão = int(input('Informe a razão da PA: '))
décimo = termo + (10 - 1) * razão
for pa in range(termo, décimo + razão, razão):
    print('{}'.format(pa), end=' >> ')
print('FIM')
