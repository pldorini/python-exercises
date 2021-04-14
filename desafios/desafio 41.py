from datetime import date
ano = int(input('Ano de nascimento: '))
an = date.today().year
n = an - ano

if n <= 9:
    print('Atleta tem {} anos. MIRIM'.format(n))
elif n <= 14:
    print('Atleta tem {} anos. INFANTIL'.format(n))
elif n <= 19:
    print('Atleta tem {} anos. JÚNIOR'.format(n))
elif n <= 25:
    print('Atleta tem {} anos. SÊNIOR'.format(n))
else:
    print('Atleta tem {} anos. MASTER'.format(n))


