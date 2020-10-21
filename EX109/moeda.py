def aumentar(valor=0, taxa=0, form=False):
    resultado =  valor + (valor * taxa / 100)
    return resultado if form == False else moeda(resultado)


def diminuir(valor=0, taxa=0, form=False):
    resultado =  valor - (valor * taxa / 100)
    return resultado if form == False else moeda(resultado)


def dobro(valor=0, form=False):
    resultado =  valor * 2
    return resultado if form == False else moeda(resultado)


def metade(valor=0, form=False):
    resultado =  valor / 2
    return resultado if form == False else moeda(resultado)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')