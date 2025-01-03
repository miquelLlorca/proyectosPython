import matplotlib.pyplot as plt 
import numpy as np

n = 0

while(True):
    n += 1
    N = n 
    pasos = []

    while(N != 1):
        pasos.append(N)
        if(N%2 == 0):
            N = int(N/2)
        else:
            N = 3*N + 1

    pasos.append(N)

    x = np.arange(0,len(pasos))

    plt.plot(x, pasos)

    if(n%10000 == 0):
        plt.show()








