s = 0
total = []
pessoa = []
cont_w = 0
cont_m = 0
name_m = ''
k = int(input('Quantas pessoas serao analsidas? '))
for c in range (1, k + 1):
    print('_' * 5, '{}° pessoa'.format(c), 5 * '_')
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Idade: ')))
    pessoa.append(str(input('Sexo [m/f]: ')).lower().strip())
    s += pessoa[1]
    total.append(pessoa[:])
    pessoa.clear()
for c in total:
    if c[2] == 'f' and c[1] < 20:
        cont_w += 1
    if c[2] == 'm' and c[1] > cont_m:
        cont_m = c[1]
        name_m = c[0]
print('{} é o mais velho e ele tem {} anos'.format(name_m, cont_m))
print('{} mulheres tem menos de 20 anos.'.format(cont_w))
print('A media de idade do grupo é {} anos'.format(s/k))
print(total)

