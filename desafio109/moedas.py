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
