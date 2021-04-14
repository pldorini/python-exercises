numero = []
ma = me = 0
for c in range(0, 5):
    numero.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        ma = me = numero[c]
    else:
        if numero[c] > ma:
            ma = numero[c]
        elif numero[c] < me:
            me = numero[c]
print('=-'*25)
print(f'Voce digitou os valores {numero}')
print(f'O maior valor digitado foi {ma} nas posições ', end='')
for i, v in enumerate(numero):
    if v == ma:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {me} nas posições ', end='')
for i, v in enumerate(numero):
    if v == me:
        print(f'{i}...', end='')