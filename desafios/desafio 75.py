cont = 0
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))
d = int(input('Digite o ultimo numero: '))
valor = (a, b, c, d)
print(f'Voce digitou os valores {valor}')
print(f'O numero 9 apareceu {valor.count(9)} vezes')

if a == 3 or b == 3or c == 3 or d == 3:
    print(f'O valor 3 apareceu na posição {valor.index(3)+1}')
else:
    print('O valor 3 nao foi digitado nenhuma vez')

print(f'Os valores pares digitados foram', end=' ')
if a % 2 == 0:
    print(f'{a}', end=' ')
if b % 2 == 0:
    print(f'{b}', end=' ')
if c % 2 == 0:
    print(f'{c}', end=' ')
if d % 2 == 0:
    print(f'{d}')
