import numpy as np
import matplotlib.pyplot as plt

def f(x):
    d = 20
    y = 1 - (d/(d**2 + x**2)**0.5)
    return y

x = np.linspace(0, 1000, 10000)

plt.plot(x, f(x))
plt.ylim(-0.05,1)
plt.show()
