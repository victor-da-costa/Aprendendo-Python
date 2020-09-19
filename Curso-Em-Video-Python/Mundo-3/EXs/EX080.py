valores = []
for cont in range(1, 6):
    num = int(input(f'Digite o {cont}º da lista: '))
    if cont == 1 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos <= len(valores):
            if num < valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
print(valores)
