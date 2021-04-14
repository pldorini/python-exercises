n = int(input('Digite um numero de 0 a 9999: '))

print('O número {} possui:'.format(n))
print('{} unidade'.format(n//1 % 10))
print('{} dezena'.format(n//10 % 10))
print('{} centena'.format(n//100 % 10))
print('{} milhar'.format(n//1000 % 10))