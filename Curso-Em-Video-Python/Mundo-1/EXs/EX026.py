frase = str(input('Digite uma frase qualquer: ')).strip().lower()
print('A letra "A" aparece {} na frase!'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('a') + 1))
print('A ultima letra "A" aparece na posição {}'.format(frase.rfind('a') + 1))