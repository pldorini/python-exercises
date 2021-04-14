def metade(n=0, format=False):
    res = n / 2
    return res if not format else moeda(res)


def aumento(n=0, taxa=0, format=False):
    res = n + (n * (taxa/100))
    return res if format is False else moeda(res)


def dobro(n=0, format=False):
    res = n * 2
    return res if not format else moeda(res)


def diminuir(n=0, taxa=0, format=False):
    res = n - (n * (taxa / 100))
    return res if format is False else moeda(res)


def moeda(n=0, moeda='R$',):
    return f'{moeda}{n:>5.2f}'.replace('.', ',')


def resumo(n=0, aum=10, red=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Aumento de {aum}%: \t{aumento(n, aum, True)}')
    print(f'Desconto de {red}%: \t{diminuir(n, red, True)}')
    print('-' * 30)
