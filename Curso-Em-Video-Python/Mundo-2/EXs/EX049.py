num = int(input('Você quer a tabuada de qual número? '))
for c in range(1, 11):
    print('{} x {} = {}'.format(c, num, c * num))