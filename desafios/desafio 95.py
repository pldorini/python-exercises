time = []
jogador = {}
gols = []
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    n = int(input(f'Quantos partidas {jogador["nome"]} jogou? '))
    for c in range(1, n + 1):
        g =  int(input(f'Quantos gols na partida {c}? '))
        gols.append(g)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    m = str(input('Quer continuar? [S/N]')).upper()[0]
    if m not in 'SN':
        m = str(input('Quer continuar? [S/N]')).upper()[0]
    if m == 'N':
        break
print('=-'*30)
print(f'{"cod":<3} {"nome":<11} {"gols":<10} {"total":>2}')
for p, v in enumerate(time):
    print(f'{p:<3}{str(v["nome"]):<11}{str(v["gols"]):^10} {str(v["total"]):>8}')
print('=-'*30)
while True:
    x = int(input('Mostrar dados de qual jogador? DIGITE 999 PARA PARAR '))
    if x == 999:
        break
    if x >= len(time):
        print('ERRO!Não existe jogador.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[x]["nome"]}')
        for p, v in enumerate(time[x]['gols']):
            print(f'No jogo {p+1} ele fez {v} gols.')
    print('=-' * 30)
print('<<<<FIM>>>>')



