def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO NÃO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


ano = int(input('Informe seu ano de nascimento: '))
print(voto(ano))
