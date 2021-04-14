from datetime import date
maior = 0
menor = 0
for c in range (1, 8):
    ano = int(input('Ano de nascimento: '))
    data = date.today().year
    idade = data - ano
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print('{} pessoas possuem mais de 18 anos'.format(maior))
print('{} pessoas possuem menos de 18 anos'.format(menor))