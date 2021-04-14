def notas(*n, sit=False):
    b = {}
    b['Total'] = len(n)
    b['Maior'] = max(n)
    b['Menor'] = min(n)
    b['Media'] = sum(n) / len(n)
    if sit:
        if b['Media'] > 7:
            b['Situação'] = 'BOA'
        elif  5 < b['Media'] < 7:
            b['Situação'] = 'RAZOÁVEL'
        elif r['Media'] < 5:
            b['Situação'] = 'RUIM'
    return b

resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)