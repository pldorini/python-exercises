n = int(input('Digite um numero inteiro: '))
print(''' Escola uma das bases para converção:
[1] Binario
[2] Octal
[3] Hexadecimal ''')
b = int(input('Sua opção: '))
if b != 1 or b != 2 or b != 3:
    print('Opção impossivel, tente novamente!')

if b == 1:
    print('{} convertido para Binario é {}'.format(n, bin(n) [2:]))
elif b == 2:
    print('{} convertido para Binario é {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('{} convertido para Binario é {}'.format(n, hex(n)[2:]))