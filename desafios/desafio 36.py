casa = float(input('Qual o valor do imovel? R$'))
salario = float(input('Qual o salario? R$'))
parc = int(input('Parcelamento de quantos anos? '))

valor = casa / (parc * 12)

if valor <= salario * 0.3:
    print('O valor de {} referente a casa sera parcelado em {}x, no valor de {:.2F}'.format(casa, parc, valor))
    print('Empréstimo APROVADO.')
else:
    print('O valor de {} referente a casa sera parcelado em {}x, no valor de {:.2f}'.format(casa, parc, valor ))
    print('Empréstimo NEGADO.')

