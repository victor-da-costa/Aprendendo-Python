num = int(input('Quantos termos a sequência de Fibonacci vai ter? '))
t1 = 0
t2 = 1
cont = 3
print('{} >> {}'.format(t1, t2), end='')
while cont < num:
    t3 = t1 + t2
    print(' >> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1