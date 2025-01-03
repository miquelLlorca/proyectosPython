from math import factorial
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

def f(x):
    d = 20
    y = 1 - (d/(d**2 + x**2)**0.5)
    return y


def fact(x):
    x = int(x)
    res = 1
    while(x>1):
        res *= x
        x -= 1

    return res


x = np.zeros(10000)
factoriales = np.zeros(10000)

for i in range(10000):
    try:
        x[i] = i
        factoriales[i] = fact(i)
    except:
        break

plt.plot(x, np.log2(x), label="log2")
plt.plot(x, np.log10(x), label="log10")

plt.plot(x, x, label="x")
#plt.plot(x, 10*x, label="10*x")

plt.plot(x, np.log(x), label="log(x)")
plt.plot(x, np.log(factoriales), label="log(x!)")
#plt.plot(x, x**2, label="x**2")
#plt.plot(x, x**3, label="x**3")
#plt.plot(x, x**4, label="x**5")
#plt.plot(x, x**5, label="x**15")
#
#plt.plot(x, x**x, label="log2")


plt.legend(loc="best")
#plt.ylim(-0.05,10000000000000)
plt.show()
