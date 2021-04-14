from datetime import date
ctps = {}
ctps['Nome'] = str(input('Nome: '))
n = int(input('Ano de Nascimento: '))
ctps['Idade'] = date.today().year - n
ctps['Carteira'] = int(input('Carteira de Trabalho (0 nao tem): '))
if ctps['Carteira'] == 0:
    for k, v in ctps.items():
        print(f'- {k} tem o valor {v}')
ctps['Contrato'] = int(input('Ano de Contratação: '))
ctps['Salário'] = int(input('Salário: R$'))

ctps['Aposentadoria'] = (ctps['Contrato'] + 35) - n
for k, v in ctps.items():
    print(f'- {k} tem o valor {v}')
print(ctps)