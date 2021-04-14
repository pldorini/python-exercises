frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]

#tanto a linha 5 como a linha 7 estao corretas!

#for c in range (len(junto) -1, -1, -1):
 #   inverso += junto[c]
if junto == inverso:
    print(junto, inverso, 'São palíndromos')
else:
    print(junto, inverso, 'Não são palindromos')