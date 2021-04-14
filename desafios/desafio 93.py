jogador = {}
gols = []
jogador['nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantos partidas {jogador["nome"]} jogou? '))
for c in range(1, n + 1):
    g =  int(input(f'Quantos gols na partida {c}? '))
    gols.append(g)
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {n} partidas') #no lugar de "n" colocar len(jogador["gols"])
for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i}, o jogador fez {v} gols ')