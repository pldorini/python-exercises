n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro numero: '))

if n1 > n2:
    print('{:.2f} é maior do que {:.2f}'.format(n1, n2))
elif n2 > n1:
    print('{:.2f} é maior do que {:.2f}'.format(n2, n1))
else:
    print('Os dois valores são iguais.')