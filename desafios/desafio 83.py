exp = str(input('Digite a expressão: '))
p = []
for símb in exp:
    if símb == '(':
        p.append('(')
    elif símb == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')