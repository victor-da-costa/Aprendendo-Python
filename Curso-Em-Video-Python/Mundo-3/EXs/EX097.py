def escreva(txt):
    print('~' * len(txt))
    print(f'{txt}')
    print('~' * len(txt))


txt = str(input('Digite sua mensagem: '))
escreva(txt)
