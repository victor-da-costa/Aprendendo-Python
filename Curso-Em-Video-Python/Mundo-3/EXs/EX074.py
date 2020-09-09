from random import randint
num = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(num)
print(f'O maior número da lista é {max(num)} e o menor número é {min(num)}')
