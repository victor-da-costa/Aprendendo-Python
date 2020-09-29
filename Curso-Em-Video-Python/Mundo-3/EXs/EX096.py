def área(largura, comprimento):
    A = largura * comprimento
    print(f'Um terreno de {largura}x{comprimento} tem uma área de {A} m2')


largura = float(input('LARGURA: [Em metros] '))
comprimento = float(input('COMPRIMENTO: [Em metros] '))
área(largura, comprimento)