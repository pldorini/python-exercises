n1 = float(input('Nota da p1: '))
n2 = float(input('Nota da p2: '))
media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi de {}, REPROVADO.'.format(media))
elif media < 7:
    print('Sua media foi de {}. RECUPERAÇÃO'.format(media))
else:
    print('Sua média foi de {}. APROVADO'.format(media))

