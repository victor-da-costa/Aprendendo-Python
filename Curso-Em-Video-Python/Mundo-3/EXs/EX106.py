def ajuda(txt):
    help(comando)


comando = ''
while True:
    comando = str(input('Função/Biblioteca >> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
