c = v = d = u = 0
while True:
    n = int(input('Qual valor deseja sacar? '))
    while n >= 50:
        n -= 50
        c += 1
    while n >= 20:
        n -= 20
        v += 1
    while n >= 10:
        n -= 10
        d += 1
    while n >= 1:
        n -= 1
        u += 1
    break
print(f'Serão entregues {c} notes de 50, {v} notas de 20, {d} notas de 10 e {u} notas de 1')