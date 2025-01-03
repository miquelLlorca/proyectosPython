# ax^2 + bx + c
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if b**2 - 4*a*c >= 0:
    x1 = (-b +(b**2 - 4*a*c)**0.5)/2*a
    x2 = (-b -(b**2 - 4*a*c)**0.5)/2*a
    print('x1 = {} , x2 = {}'.format(x1, x2))
else:
    print('error')
