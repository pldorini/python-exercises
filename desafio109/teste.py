import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando 10% temos {moedas.aumento(p, 10, True)}')
print(f'Descontando 10% temos {moedas.diminuir(p, 10, True )}')
