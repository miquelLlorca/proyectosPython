import pygame
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles


class Neural_layer(): # crear capas de una red neuronal
    def __init__(self, n_conn, n_neur, act):
        self.act = act
        self.b = np.random.rand(1, n_neur) * 2 - 1 # inicializa aleatoriamente un vector
        self.w = np.random.rand(n_conn, n_neur) * 2 - 1 # inicializa aleatoriamente una matriz
        
    def __init__(self, nl):
        self.act = nl.act
        self.b = []
        for i in range(len(nl.b)):
            self.b.append(nl.b[i] + np.random.rand() * (-1)**np.random.randint(1,2))

        self.w = []
        for i in range(len(nl.w)):
            self.w.append([])
            for j in range(len(nl.w[0])):
                self.w.append(nl.w[i][j] + np.random.rand() * (-1)**np.random.randint(1,2))
            

def createNn(tp, act): # crea red neuronal
    nn = []
    for l, layer in enumerate(tp[:-1]):
        nn.append(Neural_layer(tp[l], tp[l+1], act))
    return nn

def evolveNn(tp, NN): # evol red neuronal 
    nn = []
    for l, layer in enumerate(tp[:-1]):
        nn.append(Neural_layer(NN[l]))
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
dimensiones = [500,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()


n = 500 # numero de registros
p = 2 #caracteristica de cada registro

X, Y = make_circles(n, factor = 0.5, noise = 0.05) # n , distancia entre circulos, ruido
Y = Y[:, np.newaxis]

topology = [p, 4 , 8, 1]
gen = 0


while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    # -----------------------------------LÓGICA-----------------------------------

    if(gen == 0): # primera generacion
        NNs = []
        for i in range(10): 
            NNs.append(createNn(topology, sigm))

    loss = []
    
    for i in range(10):
        output = train(NNs[i], X, Y, cost, lr = 0.01, tr = True)
        loss.append(cost[0](output, Y))

    mejor = 0
    mejorV = 1000000000000
    for i in range(10):
        if(loss[i] < mejorV):
            mejorV = loss[i]
            mejor = i
            
    res = 50

    _x0 = np.linspace(-1.5, 1.5, res)
    _x1 = np.linspace(-1.5, 1.5, res)

    YP = np.zeros((res, res))

    for i0, x0 in enumerate(_x0):
        for i1, x1 in enumerate(_x1):
            YP[i0, i1]  = train(NNs[mejor], np.array([[x0, x1]]), Y, cost, tr=False)[0][0]

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

    ctr = 250
    esc = 145
    for i in range(len(X)): # puntos de las circ
        if(not Y[i]):
            color = [255, 0, 0]
        else:
            color = [0, 0, 255]
        pygame.draw.ellipse(pantalla, color, [ctr+X[i][0]*esc, ctr+X[i][1]*esc, 10, 10]) #color de circulo
        pygame.draw.ellipse(pantalla, (0, 0, 0), [ctr+X[i][0]*esc, ctr+X[i][1]*esc, 10, 10], 1) #borde
            

            
    pygame.display.flip()
    reloj.tick(30)








































pygame.quit()
