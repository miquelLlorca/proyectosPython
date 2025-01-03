import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects, xpos='center'): #poner una etiqueta en cada barra cambiando el lado para ponerla
    """
    Attach a text label above each bar in *rects*, displaying its height.
    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')

#definimos valores y errores
valor1, error1 = (2, 10, 20, 12, 7, 3), (1, 2, 3, 1, 2, 1)
valor2, error2 = (3, 8, 17, 11, 5, 2), (1, 3, 1, 2, 2,1)
valor3, error3 = (4, 7, 19, 15, 6, 4), (2, 1, 3, 1, 1, 2)

ind = np.arange(6)  #localizacion de barras
width = 0.3 # ancho de barras

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width, valor1, width, yerr=error1,
                color='g', label='Col1')
rects2 = ax.bar(ind, valor2, width, yerr=error2,
                color='c', label='Col2')
rects3 = ax.bar(ind + width, valor3, width, yerr=error3,
                color='r', label='Col3')
#estructura de barras
# ax.bar(posicion, valor, ancho, <barra de error, color, etiqueta,etc>)

#etiquetas y titulos
ax.set_ylabel('Valores')
ax.set_xlabel('Columnas')
ax.set_title('Ejemplo de histograma')
ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5', 'G6'))
ax.legend(loc='best')
autolabel(rects1, 'left')
autolabel(rects2, 'left')
autolabel(rects3, 'left')
plt.show()
