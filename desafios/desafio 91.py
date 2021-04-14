from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = {}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f' O {k} tirou {v}')
    sleep(0.8)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for k, v in enumerate(ranking):
    print(f'{k + 1}° lugar: {v[0]} com {v[1]}')
    sleep(0.8)