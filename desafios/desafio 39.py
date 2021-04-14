from datetime import date
ano = int(input('Ano de nascimento? '))
nom = str(input('Qual o seu genero? '))
nome = nom.lower()
atual = date.today().year
militar = atual - ano

if nome == 'masculino' and militar < 18:
    print('Voce sendo do sexo {}, deve se alistar.'.format(nome))
    print('Voce tem {} anos. Seu alistamente dever ser feito em {} anos.'.format(militar, 18 - militar))
elif nome == 'masculino' and militar == 18:
    print('Voce sendo do sexo {}, deve se alistar.'.format(nome))
    print('Voce tem 18 anos. Se aliste IMEDIATAMENTE.')
elif nome == 'masculino' and militar > 18:
    print('Voce sendo do sexo {}, deve se alistar.'.format(nome))
    print('Voce tem {} anos, deveria ter se alistado à {} anos.'.format(militar, militar - 18))
else:
    print('Voce sendo do sexo {}, nao precisa se alistar!'.format(nome))
