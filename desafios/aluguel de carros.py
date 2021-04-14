#n = int(input('Quantos dias o carro ficou alugado? '))
#n1 = float(input('Quantos Km rodados? '))
#print('O valor total a ser pago é de R${:.2F}'.format((n * 60) + (n1 * 0.15)))
from math import sqrt
n = int(input('Valor: '))
m = int(input('Valor: '))
x = sqrt(n ** 2 + m ** 2)
print(x)
