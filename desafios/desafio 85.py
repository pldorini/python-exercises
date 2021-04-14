lista = [] #ou lista[[], []] ficaria lista[0].append(x) (par) ou lista[1].append(x) (impar)
par = []
impar = []
for c in range(1, 8):
    x = int(input(f'Digite o {c}° numero:'))
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
lista.append(par)
lista.append(impar)
par.sort()
impar.sort()
print('-='*25)
print(f'Pares: {lista[0]}')
print(f'Impares: {lista[1]}')