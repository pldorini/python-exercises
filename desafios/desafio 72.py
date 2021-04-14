numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um numero entre 0 e 20:  '))

    if  n >= 0 and n <= 20:
        print(f'Voce digitou o numero {numero[n]}')

    s = str(input('Quer continuar? [s/n]')).strip().lower()
    if s == 'n':
        break

print('FIM DO PROGRAMA')