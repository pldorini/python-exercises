nome = str(input('Nome completo: ')).strip()

print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))

print('Seu nome em letras minusculas é {}'.format(nome.lower()))

print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))

lista = nome.split()
print('O seu primeiro nome é {} e possui {} letras'.format(lista[0], len(lista[0])))
