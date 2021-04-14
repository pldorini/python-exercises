
def area(x, y):
    área = x * y
    print(f'A área de um terreno de {x:.2f} x {y:.2f} é de {área} m²')

x = float(input('Largura [m]: '))
y = float(input('Comprimento [m]: '))
area(x,y)