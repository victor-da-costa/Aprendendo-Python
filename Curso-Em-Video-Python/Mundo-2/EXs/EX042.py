r1 = float(input('Informe o 1º segmento de reta: '))
r2 = float(input('Informe o 2º segmento de reta: '))
r3 = float(input('Informe o 3º segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('O segmentos formam um triângulo EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Os segmentos formam um triângulo ISÓSCELES')
    elif r1 != r2 != r3 != r1:
        print('Os segmentos formam um triângulo ESCALENO')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')