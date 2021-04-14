a = int(input('Primeiro termo da PA: '))
r = int(input('Razao da PA: '))
c = 1
while c <= 10:
    n = a + (c - 1) * r
    c += 1
    print(n, end=' -> ')
print('FIM')
#termo = a
#ou while c <= 10
#       print('{} -> '.format(termo), end='')
#       termo += r
#       c += 1
#   print('FIM')
