num = int(input('Digite um número para calcular seu Fatorial: '))
print('{}! = '.format(num), end='')
c = num
f = 1
while c > 0:
    print('{} '.format(c), end='')
#   print('x ' if c > 1 else '=', end='')
    if c > 1:
        print('x ', end='')
    else:
        print('=',end='')
    f *= c
    c -= 1
print(' {}'.format(f))
