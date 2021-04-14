from time import sleep
def contador(i, f, p):
    print('=-' * 25)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
            c += p
        print('FIM')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
            c -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 25)
print('Agora é a sua vez de personalizar a contagem!!!')
i = int(input('Valor inicial: '))
f = int(input('Valor final: '))
p = int(input('Passo: '))
contador(i, f, p)