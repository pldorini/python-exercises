from time import sleep
from random import randint
jogo = []
n = int(input('Quantos jogos voce quer que eu sorteie? '))
for c in range(1, n + 1):
    for s in range(0, 6):
        s = randint(1, 60)
        while s in jogo:
            s = randint(1, 60)
        jogo.append(s)
    sleep(0.5)
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    jogo.clear()
print('-='*5, '< BOA SORTE! >', '-='*5)