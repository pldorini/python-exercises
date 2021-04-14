from math import factorial
n = int(input('Fatorial do numero inteiro: '))
f = 0
c = n
print('O valor de {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    if c > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))



