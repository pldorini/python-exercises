s = 0
for c in range(1, 501):
    if (c % 3 == 0) and (c % 2) == 1:
        s += c
print('A soma de todos os numeros impares e multiplos de 3')
print('entre 1 e 500 é {}'.format((s)))
