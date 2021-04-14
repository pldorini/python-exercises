import random
s = cont = 0
while True:
    n = int(input('Digite um valor inteiro: '))
    p = str(input('Par ou Impar? [P/I] ')).lower().strip()
    x = random.randint(1, 2)
    s = x + n
    if s % 2 == 0 and p == 'p':
        print(f'Voce jogou {n} e o computador {x}. O total foi {s} sendo um numero PAR')
        print('Voce ganhou!!!')
        print('Vamos jogar novamente!')
        cont += 1
    elif s % 2 != 0 and p =='i':
        print(f'Voce jogou {n} e o computador {x}. O total foi {s} sendo um numero Impar')
        print('Voce ganhou!!!')
        print('Vamos jogar novamente!')
        cont += 1
    elif s % 2 == 0 and p == 'i':
        print(f'Voce jogou {n} e o computador {x}. O total foi {s} sendo um numero PAR')
        print('voce PERDEU')
        break
    elif s % 2 != 0 and p =='p':
        print(f'Voce jogou {n} e o computador {x}. O total foi {s} sendo um numero IMPAR')
        print('voce PERDEU')
        break
print(f'GAME OVER! Voce venceu {cont} vezes.')
