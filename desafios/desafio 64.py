n = s = 0
digitos = 0
while n != 999:
    n = int(input('Digite um numero inteiro, Digite 999 para parar: '))
    s += n
    digitos += 1
if n == 999:
    digitos -= 1
    s -= 999
    print('Foram digitados {} numeros e a soma deles foi {}'.format(digitos, s))
    print('FIM DO PROGRAMA')


