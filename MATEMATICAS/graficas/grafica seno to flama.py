import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10,10,1000)
plt.plot(x,np.sin(10*x)+np.sin(x), c='r')
plt.show()

plt.plot(x,x*0.5+np.sin(x), c='r')
plt.show()

x = np.linspace(-100, 100,100000)
plt.plot(x,x**2*np.sin(x), c='r')
plt.show()


#color de grafica: c='inicial color' (r,g,b, Cyan, Magenta, Yellow, blacK, White)
#otra opcion: c = '#eeefff' , html hex code
#ancho de linea: lw=numero , coge cualquier numero
