
x = 0
y = 1
n = int(input('Quantos elementos deseja? '))
c = 1
z = x + y
w = z + y
if n == 0:
    print('FIM')
else:
    print(x,'->',y, '->', z, '->', w, end=' -> ')
    if n > 4:
        if n % 2 == 0:
            while c <= (n - 4):
                z = z + w
                w = w + z
                c += 2
                print(z,'->', w, end=' -> ')
        elif n % 2 != 0:
            while c <= (n - 5):
                z = z + w
                w = w + z
                c += 2
                print(z, '-> ', w, end=' -> ')
            z = z + w
            print(z, end=' -> ')
    elif n <= 4:
        print('')
    print('FIM')