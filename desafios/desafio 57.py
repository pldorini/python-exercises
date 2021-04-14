sexo = str(input('Sexo [M/F]: ')).upper().strip( )
while sexo not in 'MF':
    sexo = str(input('Dado invalido. Digite novamente o sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))