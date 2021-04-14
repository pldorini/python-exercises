from random import randint
from time import sleep
s = 0
def sorteia(lst):
    print('Sorteando 5 valores do sorteio :',end=' ')
    for c in range(0, len(lst)):
        print(f'{lst[c]}', end=' ')
        sleep(0.5)
        print(end=' ')
    print('É isso ai!')

def somapar(par):
    print(f'Somando os valores pares da lista {numeros}, temos ', end=' ')
    print(par)


numeros = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
sorteia(numeros)
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        s += numeros[c]
somapar(s)