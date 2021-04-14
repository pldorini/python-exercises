x = int(input('Digite um valor inteiro: '))
y = int(input('Digite novamente um valor inteiro: '))
s = 0
m = 0
print('''OPERAÇÕES:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do programa''')
n = int(input('Qual operação gostaria de realizar? '))
if n > 5:
    n = int(input('Opção invalida, tente novamente. '))
elif n < 1:
    n = int(input('Opção invalida, tente novamente. '))
while 1 <= n <= 5:
    if n == 1:
        s = x + y
        print('A soma é {}'.format(s))
        n = int(input('Qual operação gostaria de realizar? '))
    elif n == 2:
        m = (x * y)
        print('A multiplicação é {}'.format(m))
        n = int(input('Qual operação gostaria de realizar? '))
    elif n == 3:
        if x > y:
            print('{} é maior do que {}'.format(x, y))
        elif y > x:
            print('{} é maior do que {}'.format(y, x))
        else:
            print('Numeros sao iguais.')
        n = int(input('Qual operação gostaria de realizar? '))
    elif n == 4:
        x = int(input('Digite um novo numero.'))
        y = int(input('Digite outro novo numero.'))
        n = int(input('Qual operação gostaria de realizar? '))
    elif n == 5:
        break
print('Fim do programa!')






