simbolos = []
expressão = str(input('Digite a expressão: '))
for simb in expressão:
    if simb == '(':
        simbolos.append(simb)
    if simb == ')':
            simbolos.pop()
if len(simbolos) == 0:
    print('Expressão valida')
else:
    print('Expressão invalida')
