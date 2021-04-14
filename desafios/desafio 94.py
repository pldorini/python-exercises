tot = {}
dados = []
totp = soma = 0
while True:
    tot['nome'] = str(input('Nome: '))
    tot['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    if tot['sexo'] not in 'MF':
        tot['sexo'] = str(input('Por favor, digite M ou F ')).upper()[0]
    tot['idade'] = int(input('Idade: '))
    soma += tot['idade']
    totp += 1
    n = str(input('Quer continuar? [S/N] '))
    dados.append(tot.copy())
    if n in 'Nn':
        break
print('=-'*30)
media = (soma / totp)
print(f'A) Ao todo temos {totp} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram', end=' ')
for c in range(0, len(dados)):
    if dados[c]['sexo'] == 'F':
        print(f'{dados[c]["nome"]}', end=', ')
print()
print('D) Lista das pessoas que estão acima da média:')
for c in dados:
    if c['idade'] >= media:
        print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
print('<< ENCERRADO >>')
