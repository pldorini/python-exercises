lista = []
pares = []
impares =[]
while True:
    lista.append(int(input('Digite um valor: ')))
    n = str(input('Quer continuar? [s/n]')).strip().lower()
    if n =='n':
        break
for c in range(0, len(lista)):
    v = lista[c]
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')