num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print('O número {} é um número primo!'.format(num))
else:
    print('O número {} não é um número primo!'.format(num))