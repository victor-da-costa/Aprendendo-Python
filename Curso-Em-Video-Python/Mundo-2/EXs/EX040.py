nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
média = (nota1 + nota2) / 2
print('tirando {:.1f} e {:.1f} a média é {:.1f}'.format(nota1, nota2, média))
if média < 5:
    print('REPROVADO')
elif média >= 5 and média < 7:
    print('RECUPERAÇÃO')
elif média > 7:
    print('APROVADO')