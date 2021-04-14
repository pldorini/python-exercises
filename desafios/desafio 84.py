grupo = []
pessoas = []
contp = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    grupo.append(pessoas[:])
    pessoas.clear()
    contp += 1
    n = str(input('Quer continuar? [S/N]'))
    if n in 'Nn':
        break
i = grupo[0][1]
j = grupo[0][1]
for c in range(0, contp):
    if c == 0:
       pesado = grupo[c][1]
       leve = grupo[c][1]

    if i > grupo[c][1]:
        pesado = i

    else:
        i = grupo[c][1]
        pesado = grupo[c][1]

    if j < grupo[c][1]:
        leve = j

    else:
        j = grupo[c][1]
        leve = grupo[c][1]

print(f'Ao todo, foram cadastradas {contp} pessoas') #possivel usar len(grupo) ao inves de contador
print(f'O mais pesado é {pesado} kg. O peso de' , end=' ')
for p in grupo:
    if p[1] == pesado:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O mais leve é {leve} kg. O peso de' , end=' ')
for p in grupo:
    if p[1] == leve:
        print(f'[{p[0]}]', end=' ')
print()



