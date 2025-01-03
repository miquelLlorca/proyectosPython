import numpy as np
import matplotlib.pyplot as plt
import funciones as f

opcion = input('Leer archivo(1) o generar numeros aleatorios(2): ')
ok = False
while not ok:
    if opcion == '1':
        x, y = f.leerArchivo()
        ok = True
    elif opcion == '2':
        x, y = f.generar()
        ok = True
    else:
        print('Opcion incorrecta.')
        opcion = input('Leer archivo(1) o generar numeros aleatorios(2): ')

    
m, b = f.ajuste(x,y)
may, men = f.maymen(x)
xA = np.linspace(men, may, 5)

plt.plot(x, y, 'ko', label='datos')
plt.plot(xA, m*xA + b, 'r', label='ajuste')
plt.legend(loc='best')
plt.show()

