import pygame
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import random 
from sklearn.datasets import make_circles


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

# funcion de coste
cost = (lambda Yp, Yr: np.mean((Yp-Yr)**2),
               lambda Yp, Yr: (Yp-Yr)) # error cuadratico medio del resultado


# -----------------------------------------------------------------------------------------------------

 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  
pygame.init()
dimensiones = [700,700]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()



def make_squares(n, factor, noise):
    X = []
    Y = []
    l = int(n/4)
    pos1 = [-1, -1]
    inc1 = 2/l
    pos2 = [-factor, -factor]
    inc2 = (2*factor)/l

    for i in range(n):
        if(i < l):      # primer lado
            X.append(np.array([-1+(-noise + random.random()*noise**2), pos1[1]]))
            Y.append(np.array([0]))

            X.append(np.array([-factor+(-noise + random.random()*noise**2), pos2[1]]))
            Y.append(np.array([1]))

            pos1[1] += inc1
            pos2[1] += inc2

        elif(i < l*2):  # segundo lado
            X.append(np.array([pos1[0], 1+(-noise + random.random()*noise**2)]))
            Y.append(np.array([0]))

            X.append(np.array([pos2[0], factor+(-noise + random.random()*noise**2)]))
            Y.append(np.array([1]))

            pos1[0] += inc1
            pos2[0] += inc2

        elif(i < l*3):  # tercer lado
            X.append(np.array([1+(-noise + random.random()*noise**2), pos1[1]]))
            Y.append(np.array([0]))

            X.append(np.array([factor+(-noise + random.random()*noise**2), pos2[1]]))
            Y.append(np.array([1]))

            pos1[1] -= inc1
            pos2[1] -= inc2

        else:           # cuarto lado
            X.append(np.array([pos1[0], -1+(-noise + random.random()*noise**2)]))
            Y.append(np.array([0]))

            X.append(np.array([pos2[0], -factor+(-noise + random.random()*noise**2)]))
            Y.append(np.array([1]))

            pos1[0] -= inc1
            pos2[0] -= inc2


    return np.array(X), np.array(Y)



n = 500 # numero de registros
p = 2 #caracteristica de cada registro

X, Y = make_circles(n, factor = 0.5, noise = 0.05) # n , distancia entre circulos, ruido
Y = Y[:, np.newaxis]

#X, Y = make_squares(n, factor = 0.5, noise = 0.05)

print(X)
#print(Y)


topology = [p, 4 , 8, 1]
NN = createNn(topology, sigm)


while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    # -----------------------------------LÓGICA-----------------------------------
    for i in range(10):
        output = train(NN, X, Y, cost, lr = 0.01, tr = True)

    res = 50

    _x0 = np.linspace(-1.5, 1.5, res)
    _x1 = np.linspace(-1.5, 1.5, res)

    YP = np.zeros((res, res))

    for i0, x0 in enumerate(_x0):
        for i1, x1 in enumerate(_x1):
            YP[i0, i1]  = train(NN, np.array([[x0, x1]]), Y, cost, tr=False)[0][0]

    # -----------------------------------DIBUJO-----------------------------------

    pantalla.fill(BLANCO)
    
    t = dimensiones[1]/len(YP)
    for i in range(len(YP)): # colormap
        for j in range(len(YP[i])):
            if(YP[i][j]<0.0625):
                color = [240, 0, 0]
            elif(YP[i][j]<0.1875):
                color = [255, 75, 75]
            elif(YP[i][j]<0.3125):
                color = [255, 150, 150]
            elif(YP[i][j]<0.4375):
                color = [255, 200, 200]
            elif(YP[i][j]<0.5625):
                color = [255, 255, 255]
            elif(YP[i][j]<0.6875):
                color = [200, 200, 255]
            elif(YP[i][j]<0.8125):
                color = [150, 150, 255]
            elif(YP[i][j]<0.9375):
                color = [75, 75, 255]
            else:
                color = [0, 0, 240]
                
            pygame.draw.rect(pantalla, color, [i*t, j*t, t, t])

    ctr = 350
    esc = 220
    for i in range(len(X)): # puntos de las circ
        if(not Y[i]):
            color = [255, 122, 235]
        else:
            color = [71, 255, 252]
        pygame.draw.ellipse(pantalla, color, [ctr+X[i][0]*esc, ctr+X[i][1]*esc, 10, 10]) #color de circulo
        pygame.draw.ellipse(pantalla, (0, 0, 0), [ctr+X[i][0]*esc, ctr+X[i][1]*esc, 10, 10], 1) #borde
            

            
    pygame.display.flip()
    reloj.tick(30)








































pygame.quit()
