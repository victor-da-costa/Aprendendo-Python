def area(largura, comprimento):
    área = largura * comprimento
    print(f'A área do terreno de {largura}m de por {comprimento}m é de {área}m2')


largura = float(input('Informe a largura do terreno: '))
comprimento = float(input('Informe o comprimento do terreno: '))
area(largura, comprimento)
