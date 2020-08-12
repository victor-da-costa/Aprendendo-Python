from math import sin, cos, tan, radians
ângulo = int(input('Digite o ângulo do qual deseja saber o sen, cos e tan: '))
print('O seno, cosseno e tangente de {} é respectivamente {:.2f}, {:.2f}, {:.2f}'.format(ângulo, sin(radians(ângulo)), cos(radians(ângulo)), tan(radians(ângulo))))