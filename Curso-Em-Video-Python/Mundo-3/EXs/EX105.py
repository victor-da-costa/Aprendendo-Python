def notas(*n, sit=False):
    quadro = {}
    quadro['total'] = len(n)
    quadro['maior'] = max(n)
    quadro['menor'] = min(n)
    quadro['média'] = sum(n) / len(n)
    if sit == True:
        if quadro['média'] >= 7:
            quadro['situação'] = 'Boa'
        elif quadro['média'] >= 5:
            quadro['situação'] = 'Razoável'
        else:
            quadro['situação'] = 'Ruim'
    return quadro


resposta = notas(5.5, 2.8, sit=True)
print(resposta)
