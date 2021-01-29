def fatorial(num, show=False):
    fat = 1
    for numero in range(num, 0, -1):
        if show:
            print(numero, end='')
            if numero > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= numero
    return fat


print(fatorial(5, show=True))
