total = []
pessoa = []
homem = mulheres = anos = 0
while True:
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade >= 18:
        anos += 1
    sexo = str(input('[M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).strip().upper()
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    pessoa.append(idade)
    pessoa.append(sexo)
    total.append(pessoa[:])
    pessoa.clear()
    x = str(input('Quer continuar? [S/N] ')).strip().upper()
    while x not in 'SN':
        x = str(input('Quer continuar? [S/N] ')).strip().upper()
    if x == 'N':
        print(total)
        print('FIM DO PROGRAMA!')
        print(f'Total de pessoas com mais de 18 anos: {anos}')
        print(f'Ao todo, temos {homem} homens cadastrados')
        print(f'Temos {mulheres} mulheres com menos de 20 anos')
        break
