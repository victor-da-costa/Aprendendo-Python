def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


print(voto(1850))
