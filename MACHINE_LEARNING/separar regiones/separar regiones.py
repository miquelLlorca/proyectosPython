import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

import time
from IPython.display import clear_output


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
                deltas.insert(0, cost[1](a, y) * nn[i].act[1](a)) # funcion calculo delta dC * dAct
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

X, Y = make_circles(n, factor = 0.5, noise = 0.05) # n , distancia entre circulos, ruido
Y = Y[:, np.newaxis]

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

        fig, (ax0, ax1) = plt.subplots(ncols=2)
        
        ax0.pcolormesh(_x0, _x1, YP, cmap="RdBu")
        
        ax0.axis("equal")
        ax0.scatter(X[Y[:,0]==0, 0], X[Y[:,0]==0,1], c = 'salmon')
        ax0.scatter(X[Y[:,0]==1, 0], X[Y[:,0]==1,1], c = 'skyblue')

        clear_output(wait=True)
        ax1.plot(range(len(loss)), loss)
        plt.show()
        time.sleep(0.5)

        

'''
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu,
BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens,
Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn,
PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG,
PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r,
Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu,
RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r,
Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r,
YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r,
binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool,
cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r,
flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r,
gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg,
gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r,
hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r,
ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r,
seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r,
tab20b, tab20b_r, tab20c, tab20c_r, terrain,terrain_r, twilight, twilight_r, twilight_shifted,
twilight_shifted_r, viridis, viridis_r, winter, winter_r
# plot del dataset


plt.show()
'''
