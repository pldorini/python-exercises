from random import randint
from time import sleep
num = randint(0,5)
print('=-' * 31)
print('Escolhi um numero de 0 á 5, consegue adivinhar qual eu escolhi? ')
print('=-' * 31)
n = int(input('Escolha um numero de 0 á 5: '))
print('Processando...')
sleep(2)
print(' ')
if n == num:
     print('Parabéns! Você acertou')
else:
    print('Que pena, errou. O numero escolhido foi {}'.format(num))
