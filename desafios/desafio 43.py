p = float(input('Qual é o seu peso em kg? '))
h = float(input('Qual é a sua altura em m? '))
imc = p / (h ** 2)
print('Seu indice de massa corporal é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif imc < 25:
    print('Voce esta no peso ideal.')
elif imc < 30:
    print('Voce esta com sobrepeso.')
elif imc < 40:
    print('Voce esta com obesidade.')
else:
    print('Voce esta com obesidade mórbida.')

