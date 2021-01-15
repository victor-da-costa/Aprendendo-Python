expressao = str(input('Digite a expressao matemática: '))
cont = []
for simbolo in expressao:
    if simbolo == '(':
        cont.append('(')
    elif simbolo == ')':
        if len(cont) > 0:
            cont.pop()
        else:
            cont.append(')')
            break
if len(cont) == 0:
    print('A expressão matemática é válida!!!')
else:
    print('A expressão matemática é invalida!!!')
