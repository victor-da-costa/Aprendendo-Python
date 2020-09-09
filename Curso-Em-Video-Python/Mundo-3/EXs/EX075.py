num = (int(input('Digite o 1º número: ')), 
int(input('Digite o 2º número: ')), 
int(input('Digite o 3º número: ')), 
int(input('Digite o 4º número: ')))
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na posição {num.index(3)+1}')
else:
    print('O número 3 não foi digitado')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
