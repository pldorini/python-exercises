nome = str(input('Digite o nome completo: ')).strip()
n = nome.split()

print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))