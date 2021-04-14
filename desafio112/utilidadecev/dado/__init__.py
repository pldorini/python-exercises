def leiadinheiro(n,):
    valido = False
    while not valido:
        pre = str(input(n)).replace(',', '.').strip()
        if pre.isalpha() or pre == '':
            print(f'ERRO! \"{pre}\" é um preço inválido!')
        else:
            valido = True
            return float(pre)
