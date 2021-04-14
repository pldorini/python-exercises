tupla = ('Monica', 'Ornella', 'vovo', 'titio','papai', 'dindo', 'dinda', 'bebe',)
for c in tupla:
     print(f'\nA palavra {c.upper()} possui as vogais', end=' ')
     for vogal in c:
         if vogal.lower() in 'aeiou':
             print(vogal, end=' ')
