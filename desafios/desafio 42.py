from math import sqrt
r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('equilátero')
    elif r1 != r2 != r3 != r1:
        print('escaleno.')
        if r1 ** 2 == (r2 ** 2 + r3 ** 2) or r2 ** 2 == (r1 ** 2 + r3 ** 2) or r3 ** 2 == (r2 ** 2 + r1 ** 2):
            print('Do tipo Retângulo')
        else:
            print('E nao é do tipo retangulo')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('isósceles.')
else:
    print("Não formam um triângulo")



