import numpy as np

# PROBLEMA: 
# tenemos 25 caballos, queremos saber los 3 mas rapidos
# no tenemos reloj y solo podemos hacer carreras de 5 en 5

caballos = [np.random.randint(50, 100) for i in range(25)]
grupos = []

print(caballos)
print()

for i in range(5):
    grupos.append([])

    longitud = 1000
    pos = [0, 0, 0, 0, 0]

    while(len(grupos[i]) < 5):
        for j in range(5):
            if(pos[j] < longitud):
                pos[j] += caballos[i*5 + j]

                if(pos[j] > longitud):
                    for p in range(len(grupos[i])):
                        if(grupos[i][p+1] < caballos[i*5 + j]):
                            grupos[i].insert(caballos[i*5 + j], p)

for i in range(5):

        
print(grupos)
