import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y =  20*x - x**2
    return y

def g(x):
    y = 2*x**2 -40*x + 400
    return y

def h(x):
    y = x**3 + x**2 - 40*x + 400
    return  y

def zero(x):
    return x*0

def df(x):
    return 2*(10 - x)

def dg(x):
    return 4*(x - 10)

def dh(x):
    return 3*x**2 + 2*x - 40

x = np.linspace(-10,15,1000)

plt.subplot(121)
plt.plot(x, f(x), c = 'r', label = '$f(x)$')
plt.plot(x, g(x), c = 'b', label = '$g(x)$')
plt.plot(x, h(x), c = 'g', label = '$h(x)$')
plt.plot(x, zero(x), c = 'k', lw= 0.5)
plt.legend(loc = 'best')
#plt.ylim(-1000,1000)
#plt.xlim(9,11)

plt.subplot(122)
plt.plot(x, zero(x), c = 'k', lw= 0.5)
plt.plot(x, df(x), c = 'r', label = "$f'(x)$")
plt.plot(x, dg(x), c = 'b', label = "$g'(x)$")
plt.plot(x, dh(x), c = 'g', label = "$h'(x)$")
plt.legend(loc = 'best')
plt.show()
