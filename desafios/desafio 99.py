from time import sleep
def maior(*num):
    if len(num) == 0:
        print('=-' * 25)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi 0')

    else:
        print('=-' * 25)
        print('Analisando os valores...')
        for c in range(0, len(num)):
            print(f'{num[c]}', end=' ')
            sleep(0.5)
        print(end=' ')
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()