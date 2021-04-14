
n = int(input('Digite um numero inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

