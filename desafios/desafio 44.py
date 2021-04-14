print('~' * 20, 'LOJAS SENNA /A/', '~' * 20)
p = float(input('Valor da compra. R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista no cartão
[ 3 ] até 2x no cartão
[ 4 ] 3x ou mais ''')
f = int(input('Qual a opção? '))

if f == 1:
    n1 = p * 0.9

    print('Sua compra de R${:.2F} custará R${:.2F}'.format(p, n1))

elif f == 2:
    n2 = p * 0.95
    print('Sua compra de R${:.2F} custará R${:.2F}'.format(p, n2))

elif f == 3:
        print('Sua compra custou R${:.2F}'.format(p))

elif f == 4:
    n4 = p * 1.20
    print('Sua compra de R${:.2F} custará R${:.2F}'.format(p, n4))
    b = int(input(('''Parcelamento:
    [3] 3x 
    [4] 4x
    [5] 5x
    [6] 6x
    Dividir em: ''')))
    if b == 3:
        b3 = n4 / 3
        print('Sera cobrado 3 parcelas de R${}'.format(b3))

    elif b == 4:
        b4 = n4 / 4
        print('Sera cobrado 4 parcelas de R${}'.format(b4))

    elif b == 5:
        b5 = n4 / 5
        print('Sera cobrado 5 parcelas de R${}'.format(b5))

    elif b == 6:
        b6 = n4 / 6
        print('Sera cobrado 6 parcelas de R${}'.format(b6))




