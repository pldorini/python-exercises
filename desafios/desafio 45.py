from random import randint
lista = ['pedra', 'papel', 'tesoura']
pc = randint(0,2)
print('''Opções:
[0] Pedra
[1] Papel 
[2] Tesoura''')
n = int(input('Qual a sua jogada? '))

print('''JO
KEN
PO!!!''')

print('~' * 20)
if (n == 0) and pc == 1:
    print('Computador escolheu {}.PERDEU'.format(lista[pc]))
elif (n == 1) and pc == 2:
    print('Computador escolheu {}.PERDEU'.format(lista[pc]))
elif (n == 2) and pc == 0:
    print('Computador escolheu {}.PERDEU'.format(lista[pc]))
elif (n == 0) and pc == 2:
    print('Computador escolheu {}.GANHOU'.format(lista[pc]))
elif (n == 1) and pc == 0:
    print('Computador escolheu {}.GANHOU'.format(lista[pc]))
elif (n == 2) and pc == 1:
    print('Computador escolheu {}.GANHOU'.format(lista[pc]))
elif n > 2:
    print('Opção invalida, tente novamente.')
else:
    print('Quase. EMPATOU!!')
print('~' * 20)


