r1 = float(input('Informe o 1º segmento: '))
r2 = float(input('Informe o 2º segmento: '))
r3 = float(input('Informe o 3º segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmentos PODEM formar um triângulo')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')