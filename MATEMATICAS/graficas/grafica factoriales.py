import numpy as np
import matplotlib.pyplot as plt

def factorial(x):
    fact = 1
    for i in range(int(x), 1, -1):
        fact *= i
    return fact


x = np.linspace(1, 5000, 5000)
y = []
for X in x:
    y.append(len(str(factorial(X))))
    
plt.plot(x,y, 'r-o', lw=1, label='$x$')
plt.xlim(0, 16000)
plt.show()
'''
t = np.linspace(0,4,8)
plt.plot(t, t**2, 'k-o') # o = circulo, ^ = triangulo, s = cuadrado, -- = linea disc, -o = linea con puntos
plt.show()
#color de grafica: c='inicial color' (r,g,b, Cyan, Magenta, Yellow, blacK, White)
#otra opcion: c = '#eeefff' , html hex code
#ancho de linea: lw=numero , coge cualquier numero
'''
