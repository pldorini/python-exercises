aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
a = float(input('Nota da p1: '))
b = float(input('Nota da p2: '))
media = (a + b) / 2
aluno['media'] = media
print(f'- Nome é {aluno["nome"]}')
print(f'- média é igual a {aluno["media"]}')
if media >= 7:
    print('- Aluno está aprovado!')
else:
    print('- Aluno reprovado')