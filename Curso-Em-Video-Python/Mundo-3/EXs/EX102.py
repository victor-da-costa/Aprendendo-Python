def fatorial(num, show=False):
    fat = 1
    for valor in range(num, 0, -1):
        if show:
            print(valor, end='')
            if valor > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= valor
    return fat


print(fatorial(7, show=True))