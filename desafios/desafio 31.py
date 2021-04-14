n = int(input('Qual a distancia da viagem em km? '))
if n<=200:
    c = 0.5 * n
    print('O valor da passagem é de {}'.format(c))
else:
    p = 0.45 * n
    print('O valor da passagem é de {}'.format(p))