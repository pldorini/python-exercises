n = float(input('Qual o salário? R$'))

if n > 1250.00:
    print('Voce ganhou um aumento de R${:.2f}, seu novo salario é de R${}'.format(n * 0.1, n * 1.1))
else:
    print(f'Voce ganhou um aumento de R${n * 0.15:.2f}, seu novo salario é de R${n * 1.15}')
