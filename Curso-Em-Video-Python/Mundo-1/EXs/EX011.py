largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura * largura
litros = area / 2
print('Para pintar uma parede de {}x{} com uma area total de {}m2 é necessario {}l de tinta'.format(largura, altura, area, litros))