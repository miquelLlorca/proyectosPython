import numpy as np
from os import system


data = [0, 0, 0, 0, 0, 0]
stats = np.zeros(150, int)
total = 0

while(True):
    lanzada = np.random.randint(0, 6)
    
    for i in range(6):
        if(i == lanzada):
            stats[data[i]] += 1
            data[i] = 0
        else:
            data[i] += 1

    total += 1

    if(total%1000 == 0):
        system("clear")
        for i in range(150):
            if(stats[i] != 0):
                print(f"{i}:{stats[i]}", end=" // ")