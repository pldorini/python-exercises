a = int(input('Primeiro termo da PA: '))
r = int(input('Razao da PA: '))
for c in range (1, 11,):
    n = a + (c - 1) * r
    print(n, end=' / ')
#OU a=......
#   r=...........
#   for ce in range(a, 10, r):
# print(n, end=' / ')