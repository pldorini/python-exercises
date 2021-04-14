a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))

if a > b and a > c:
    print('{} é o maior numero'.format(a))
else:
    print('')

if b > a and b > c:
    print('{} é o maior numero.'.format(b))
else:
    print('')

if c > a and c > b:
    print('{} é o maior numero'.format(c))
else:
    print('')

if a < b and a < c:
    print('{} é o menor numero'.format(a))
else:
    print('')

if b < a and b < c:
    print('{} é o menor numero'.format(b))
else:
    print('')

if c < a and c < a:
    print('{} é o menor numero'.format(a))
else:
    print('')