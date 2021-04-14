import moedas

p = float(input('Digite o preço: R$'))
tax = int(input('Taxa: '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando {tax}% temos {moedas.moeda(moedas.aumento(p, tax))}')
print(f'Descontando {tax}% temos {moedas.moeda(moedas.diminuir(p, tax))}')
