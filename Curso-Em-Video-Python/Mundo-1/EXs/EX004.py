algo = input('Digite algo: ')
print('''O tipo primitivo do que foi digitado é {},
Só tem espaço? {};
É um número? {};
É alfabético? {};
É alfanumérico? {};
Está em letras maiúsculas? {};
Está em letras minusculas? {};
Está capitalizada? {}.'''.format(type(algo), algo.isspace(), algo.isnumeric(), algo.isalpha(), algo.isalnum(), algo.isupper(), algo.islower(), algo.istitle()))