for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=' ')
print('FIM')

# A segunda solução é melhor pois são feitos menos "for" exigindo menos do computador.

for num in range(2, 51, 2):
    print(num, end=' ')
print('FIM')