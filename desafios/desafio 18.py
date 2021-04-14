import math
n = float(input('Valor do ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O valor do seno de {} é {:.2f}, o valor do cosseno é {:.2f} e sua tangente é {:.2f}'.format(n, sen, cos, tan))
