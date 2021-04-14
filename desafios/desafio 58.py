from random import randint
from time import sleep
count = acerto = 1
a = randint(0, 10)
print('\033[4:31m-\033[m' * 55)
print('Escolhi um numero entre 0 e 10, quantas tentativas acha que acerta?')
print('\033[4:31m-\033[m' * 55)
n = int(input('Digite um numero inteiro entre 0 e 10: '))
print('Processando...')
sleep(1)
while n != a:
    print('\033[1:31:43mERROU! TENTE NOVAMENTE\033[m')
    n = int(input('Digite um numero inteiro entre 0 e 10: '))
    print('Processando...')
    sleep(1)
    count += 1
if n == a:
    if count == 0:
        aprov = acerto
    aprov = (acerto / count) * 100
    if aprov == 100:
        print('\033[4:31mPARABENS, ACERTOU\033[m após {} tentativa, seu aproveitamento foi de {}%'.format(count, aprov ))
    else:
        print('\033[4:31mPARABENS, ACERTOU\033[m após {} tentativas, \n'
        'seu aproveitamento foi de {:.2f}%'.format(count, aprov ))
