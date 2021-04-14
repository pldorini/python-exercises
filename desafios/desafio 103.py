def ficha(nome, gol):
    print(f' O jogador {nome} fez {gol} gol(s) no campeonato')


n = str(input('Nome do Jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    n = '<Desconhecido>'
    ficha(n, g)
else:
    ficha(n, g)