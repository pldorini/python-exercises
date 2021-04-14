lista = [ [0, 0, 0 ], [0, 0, 0], [0, 0, 0] ]
spares = somac = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para {l, c}: '))
print('-='*25)
for l in range(0, 3):
    for c in range(0, 3):
       print(f'[{lista[l][c]:^5}]', end='')
    print()
print('-='*25)
par = []
for l in range(0, 3):
    for c in range(0, 3):
        if lista[l][c] % 2 == 0:
           par.append(lista[l][c])
for v in par:
    spares += v

print(f'A soma dos numeros pares é {spares}')
for l in range(0, 3):
    somac += lista[l][2]
print(f'A soma dos elementos da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {max(lista[1])}')
