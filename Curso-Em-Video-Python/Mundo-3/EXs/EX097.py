def escreva(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))


txt = str(input('Escreva a mensagem: ')).upper()
escreva(txt)
