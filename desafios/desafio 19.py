import random
um = str(input('Primeiro aluno: '))
dois = str(input('Segundo aluno: '))
tres = str(input('Terceiro aluno:'))
quatro = str(input('Quarto aluno: '))
lista = [um, dois, tres, quatro]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

