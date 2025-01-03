import numpy as np
import matplotlib.pyplot as plt

nums = []
sumas = []
suma = 0
for i in range(0, 10000000):
    x = str(i)
    for j in x:
        suma += int(j)**int(j)

    nums.append(i)
    sumas.append(suma)
    if suma == i:
        print(i, '- True')
    else:
        print(i)
    suma = 0
    
'''
x = np.linspace(2220, 2230, 10)

plt.plot(x, nums, 'bo')
plt.plot(x, sumas, 'go')
plt.show()

'''
