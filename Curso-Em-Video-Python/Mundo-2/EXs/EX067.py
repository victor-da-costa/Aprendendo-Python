while True:
    num = int(input('Você quer a tabuada de que número? '))
    if num < 0:
        break
    print('=' * 15)
    for t in range(1, 11):
        print(f'{num}x{t} = {num * t}')
    print('=' * 15)
print('FIM DO PROGRAMA')