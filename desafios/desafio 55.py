lista = []
for c in range (1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    lista += [peso]
print('')
print('O maior valor da lista foi {}'.format(max(lista)))
print('O menor valor da lista foi {}'.format(min(lista)))

#maior = 0
#menor = 0
#for p in range (1, 6):
#    peso = float(input('Peso da {}° pessoa: '.format(c)))
#       if p == 1:
#       maior = peso
#       menor = peso
#       else:
#           if peso > maior:
#               maior = peso
#           if peso < menor:
#               menor = peso
#

