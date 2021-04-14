print('*' * 32)
print('{:6}'.format(''), 'TABELA DE PREÇOS')
print('*' * 32)
lista = ('Lapis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20', 'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')

for c in range (0, 18, 2):
    print('{:.<15}'.format(lista[c]), 'R$','{:>6}'.format(lista[c + 1]))





