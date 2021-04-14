def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if  idade < 18:
        return f'Com {idade} anos: Não VOTA'
    elif idade > 18 and idade < 65:
       return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'

n = int(input('Ano de Nascimento: '))
print(voto(n))