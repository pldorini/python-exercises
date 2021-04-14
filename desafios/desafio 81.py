lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    n = str(input('Quer continuar? [s/n]')).strip().lower()
    if n not in 'sn':
        n = str(input('Quer continuar? [s/n]')).strip().lower()
    if n == 'n':
        break
print(f'Quantidade de números digitados foi {len(lista)}')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista, e está na posição', end=' ')
    for i, v in enumerate(lista):
        if v == 5:
            print(f'{i}...', end='')
else:
    print('O valor 5 não foi encontrado na lista.')


        
        