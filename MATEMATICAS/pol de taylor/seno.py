import numpy as np
import matplotlib.pyplot as plt

def fact(m):
    sol = 1
    for i in range(m):
        sol *= (i+1)
    return sol

def taylor(x, n):
    sol = x
    masmen = 0
    for i in range(3,n):
        if (i+5)%4 == 3:
            term = (x**(i+1))/(fact(i+1))
            sol -= term
        elif (i+5)%4 == 1:
            term = (x**(i+1))/(fact(i+1))
            sol += term
    return sol

n = 15 # int(input())

px = 1
y = taylor(px, n)

while -3 < y < 3 :
    px += 1
    y = taylor(px, n)
print(px)
x = np.linspace(-px, px, 1000)


plt.plot(x, np.sin(x))
plt.plot(x, taylor(x, n))
plt.ylim(-3, 3)
plt.show()
