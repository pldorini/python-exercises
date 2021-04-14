n = int(input('A que velocidade o carro estava em Km/h? '))
if n <= 80:
    print('Dirija com segurança!')
else:
    m = (n - 80)*7
    print('Você foi multado pois estava á {} km/h'.format(n))
    print('A multa é de R${}'.format(m))

