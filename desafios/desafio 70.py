valort = qnt = valorm = barato = qntm = 0
b = ''
while True:
    p = str(input('Produto comprado: ')).strip()
    v = float(input('Valor do produto: '))
    valort += v

    if v > 1000:
        valorm += 1
        qntm += 1
    qnt += 1
    if qnt == 1 or v < barato:
        barato = v
        b = p

    n = str(input('Quer continuar? [s/n]')).strip().lower()[0]
    while n not in 'sn':
        n = str(input('Quer continuar? [s/n]')).strip().lower()[0]

    if n == 'n':
        print(f'O total da compra foi de R${valort:.2f}')
        print(f'Temos {qntm} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {b} que custa R${barato}')
        break