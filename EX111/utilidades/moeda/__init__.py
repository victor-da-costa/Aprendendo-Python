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
    

def resumo(valor=0, aum=10, dim=10):
    print('=' * 50)
    print('RESUMO'.center(50))
    print('=' * 50)
    print(f'>> Dobro:\t\t{dobro(valor, True)}')
    print(f'>> Metade:\t\t{metade(valor, True)}')
    print(f'>> {aum}% aumento:\t\t{aumentar(valor, 10, True)}')
    print(f'>> {dim}% redução:\t\t{diminuir(valor, 10, True)}')