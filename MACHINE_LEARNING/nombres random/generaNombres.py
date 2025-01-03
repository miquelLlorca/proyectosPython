import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

import time



class Neural_layer(): # crear capas de una red neuronal
    def __init__(self, n_conn, n_neur, act):
        self.act = act
        self.b = np.random.rand(1, n_neur) * 2 - 1 # inicializa aleatoriamente un vector
        self.w = np.random.rand(n_conn, n_neur) * 2 - 1 # inicializa aleatoriamente una matriz


def createNn(tp, act): # crea red neuronal
    nn = []
    for l, layer in enumerate(tp[:-1]):
        nn.append(Neural_layer(tp[l], tp[l+1], act))
    return nn


def train(nn, x, y, cost, lr=0.5, tr = True): # lr = learning rate (alpha en descenso gradiente)

    # forward pass
    # pasar los valores por la red

    out = [[0, x]]
    for l, layer in enumerate(nn):
        z = out[-1][1] @ nn[l].w + nn[l].b # suma ponderada
        a = nn[l].act[0](z) # funcion de activacion
        out.append([z, a])

    if(tr):
        # back propagation
        
        deltas = []
        for i in reversed(range(0, len(nn))):
            z = out[i+1][0]
            a = out[i+1][1]
            
            if(i == len(nn)-1): # delta ultima capa
                deltas.insert(0, cost[1](a, Y) * nn[i].act[1](a)) # funcion calculo delta dC * dAct
            else: # delta respecto a capa previa
                deltas.insert(0, deltas[0] @ WP * nn[i].act[1](a)) # funcion calculo delta dC * dAct

            WP = nn[i].w.T
        
            # descenso gradiente
            nn[i].b = nn[i].b - np.mean(deltas[0], axis=0, keepdims=True) * lr
            nn[i].w = nn[i].w - out[i][1].T @ deltas[0] * lr

    return out[-1][1]

    
# Funciones de activacion

sigm = (lambda x: 1/(1+np.e**(-x)),
            lambda x: x*(1-x)) # sigmoide y derivada

relu = lambda x: np.maximum(0, x) # relu


# funcion de coste
cost = (lambda Yp, Yr: np.mean((Yp-Yr)**2),
               lambda Yp, Yr: (Yp-Yr)) # error cuadratico medio del resultado



# MAIN  ----------------------------------------------------------------------------------------------
        
n = 500 # numero de registros
p = 2 #caracteristica de cada registro

X, Y = 
Y = 





topology = [p, 4 , 8, 1]
NN = createNn(topology, sigm)
loss = []






for i in range(10000):
    output = train(NN, X, Y, cost, lr = 0.01, tr = True)

    if(i%50==0):
        loss.append(cost[0](output, Y))

        res = 50

        _x0 = np.linspace(-1.5, 1.5, res)
        _x1 = np.linspace(-1.5, 1.5, res)

        YP = np.zeros((res, res))

        for i0, x0 in enumerate(_x0):
            for i1, x1 in enumerate(_x1):
                YP[i0, i1]  = train(NN, np.array([[x0, x1]]), Y, cost, tr=False)[0][0]

        

        
