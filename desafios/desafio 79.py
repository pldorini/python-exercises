lista = []
while True:
    x = (int(input('Digite um valor: ')))
    if x in lista:
        print('Valor duplicado, sem alterações')
    else:
        lista.append(x)
        print('Valor adicionado com sucesso...')
    n = str(input('Quer continuar? [S/N] ')).strip()
    if n in 'Nn':
        break
lista.sort()
print(f'Voce digitou os valores {lista}')
