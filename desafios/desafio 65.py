c = ''
a = cont = soma = maior = media = menor = 0
while c != 'n':
    c = str(input('Quer digitar mais valores, [s/n]? ')).lower().strip()
    if c == 's':
        n = float(input('Digite um valor: '))
        soma += n
        cont += 1
        if n < a:
            menor = n
        elif n > a:
            maior = n
            a = n
    media = soma / cont
    if c == 'n':
        print('Fim do programa.')
        break
print('A media de todos os {} valores é de {:.2f}'.format(cont, media))
print('enquanto o maior valor foi {} e o menor foi {}'.format(maior, menor))
