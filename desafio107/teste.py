import moedas

num = float(input('Digite o preço: R$'))
tax = float(input('Taxa: '))
print(f'A metade de R${num:.2f} é R${moedas.metade(num)}')
print(f'O dobro de R${num:.2f} é R${moedas.dobro(num)}')
print(f'Aumentando {tax}% temos R${moedas.aumento(num, tax):.2f}')
print(f'Descontando {tax}% temos R${moedas.diminuir(num, tax):.2f}')