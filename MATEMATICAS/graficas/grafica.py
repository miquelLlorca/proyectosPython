import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10,10,1000)
plt.plot(x,x, c='r', lw=1, label='$x$')
plt.plot(x, x**2, c='b', lw=2, label='$x^2$')
plt.plot(x,x**3, c='g', lw=3, label='$x^3$')
plt.plot(x,x**4, c='y', lw=4, label='$x^4$')
plt.plot(x,x**5, c='m', lw=5, label='$x^5$')
plt.plot(x,x**6, c='c', lw=6, label='$x^6$')
plt.legend(loc='best')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.ylim(0,1)
plt.xlim(0,1)
plt.show()

t = np.linspace(0,4,8)
plt.plot(t, t**2, 'k-o') # o = circulo, ^ = triangulo, s = cuadrado, -- = linea disc, -o = linea con puntos
plt.show()
#color de grafica: c='inicial color' (r,g,b, Cyan, Magenta, Yellow, blacK, White)
#otra opcion: c = '#eeefff' , html hex code
#ancho de linea: lw=numero , coge cualquier numero
