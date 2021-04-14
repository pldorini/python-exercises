boletim = []
media = cont = 0
while True:
    aluno = (str(input('Nome: ')))
    p1 = float(input('Nota 1: '))
    p2 = float(input('Nota 2: '))
    media = (p1 + p2)/ 2
    boletim.append([aluno, [p1, p2], media])
    cont += 1
    n = str(input('Quer continuar? [S/N]'))
    if n in 'Nn':
        break
print(f'{"No.":<3}{"Nome":<10}{"Nota":>8}')
print('-'*20)
for p, v in enumerate(boletim):
    print(f'{p:<3}{v[0]:<10}{v[2]:>8}')
print('-'*20)
while True:
    x = int(input('Mostrar notas de qual aluno? (digite -1 para interromper): '))
    if x <= len(boletim) - 1:
        print(f'Notas de {boletim[x][0]} são {boletim[x][1]}')
        print('-'*20)
    if x == -1:
         break
print('  Finalizando...')
print('<<Volte sempre>>')