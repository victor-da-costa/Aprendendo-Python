sexo = str(input('Informe o sexo: [M/F] ')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('Dado invalido, Informe o sexo: [M/F] ')).strip().upper()
print('O sexo {} foi registrado com sucesso'.format(sexo))
