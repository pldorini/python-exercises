x = str(input('Digite uma frase: ')).strip().upper()

print('A letra', '"a"', 'aparece {} vezes'.format(x.count('A')))

print('A letra "a" aparece na posição {} na primeira vez'.format(x.find('A')+1))

print('A letra "a" aparece na posição {} na ultima vez'.format(x.rfind('A')+1))