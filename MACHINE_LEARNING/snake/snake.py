import pygame
from random import randrange
import pygame
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles


class Neural_layer(): # crear capas de una red neuronal
    def __init__(self, b, w, act):
        self.act = act
        self.b = b
        self.w = w


def createNnP(tp, act): # crea red neuronal
    nn = []
    for l, layer in enumerate(tp[:-1]):
        b = (np.random.rand(1, tp[l+1]) * 2 - 1)[0] # inicializa aleatoriamente un vector
        w = np.random.rand(tp[l], tp[l+1]) * 2 - 1 # inicializa aleatoriamente una matriz
        nn.append(Neural_layer(b, w, act))
    return nn


def createNnH(tp, act, padre, er): # crea red neuronal
    nn = []
    for l, layer in enumerate(tp[:-1]):
        b = []

        for i in range(tp[l+1]):
            b.append(padre[l].b[i] + np.random.rand()*er)

        w = []
        for i in range(tp[l]):
            w.append([])
            for j in range(tp[l+1]):
                w[i].append(padre[l].w[i][j] + np.random.rand()*er)
            
        nn.append(Neural_layer(b, w, act))
    return nn



def train(nn, x, cost, lr=0.5, tr = True): # lr = learning rate (alpha en descenso gradiente)

    out = [[0, x]]
    for l, layer in enumerate(nn):
        z = out[-1][1] @ nn[l].w + nn[l].b # suma ponderada
        a = nn[l].act[0](z) # funcion de activacion
        out.append([z, a])

    return out[-1][1]

    
# Funcion de activacion

sigm = (lambda x: 1/(1+np.e**(-x)),
            lambda x: x*(1-x)) # sigmoide y derivada

# funcion de coste
cost = (lambda Yp, Yr: np.mean((Yp-Yr)**2),
               lambda Yp, Yr: (Yp-Yr)) # error cuadratico medio del resultado






#-----------------------------------------------------------------------------------------------------------------------------
def creaCom():
    x = [randrange(1,46)*15, randrange(1,46)*15]
    while x in cola:
        x = [randrange(1,46)*15, randrange(1,46)*15]
    return x

def bordes():
    pygame.draw.rect(pantalla, (255,255,255), [0, 0, 14, 704])
    pygame.draw.rect(pantalla, (255,255,255), [0, 0, 704, 14])
    pygame.draw.rect(pantalla, (255,255,255), [705, 705, -13, -705])
    pygame.draw.rect(pantalla, (255,255,255), [705, 705, -705, -13])
    
NEGRO = (0, 0 ,0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

vel = [0,0]
puntos = 0
cola = []
for i in range(3):
    cola.append([-1*(i-1)*15, 15])
perder = False
posCom = creaCom()

pygame.init()
dimensiones = [705,705] #47 cuadrados de 15 px
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Snake')
hecho = False
reloj = pygame.time.Clock()




p = 4 #inputs para la ia
'''
x
y
dx = distancia en x hasta comida
dy = distancia en y hasta comida

'''

er = 0.5
topology = [p, 10 , 15, 10, 2]

ia = 0
generacion = 1
print("------------------- GENERACION 1 -------------------")
poblacion = 10

nns = []
for i in range(10):
    nns.append(createNnP(topology, sigm))
pts = []

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            '''
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                if vel[0] == 0:
                    vel = [-1,0]
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                if vel[0] == 0:
                    vel = [1,0]
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                if vel[1] == 0:
                    vel = [0,-1]
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                if vel[1] == 0:
                    vel = [0,1]
            '''
            if evento.key == pygame.K_r: #reset
                vel = [0,0]
                puntos = 0
                cola = []
                for i in range(3):
                    cola.append([-1*(i-1)*15, 15])
                perder = False
                posCom = creaCom()

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    
    if not perder:
        #ia
        dx = cola[0][0] - posCom[0]
        dy = cola[0][1] - posCom[1]
        vel = train(nns[ia], np.array([[cola[0][0], cola[0][1], dx, dy]]),  cost, tr=False)[0]
    
            
        # cosas del juego
        if vel[0] != 0 or vel[1] != 0:
            if cola[len(cola)-1] == [None]:
                cola[len(cola)-1] = [cola[len(cola)-2][0], cola[len(cola)-2][1]]
            for i in range(len(cola)-1,-1, -1):
                if i < len(cola)-1:
                    cola[i+1] = [cola[i][0], cola[i][1]]
                
            for i in range(2):
                if 15 <= cola[0][i] + vel[i] <= dimensiones[i] - 30:
                    for j in range(1,len(cola)):
                        if cola[j][0] == cola[0][0] + vel[0]*15 and cola[j][1] == cola[0][1] + vel[1]*15:
                            perder = True
                            break
                            
                    if not perder:
                        cola[0][i] += vel[i]*15
                else:
                    perder = True
                    break
        if posCom == cola[0]:
            posCom = creaCom()
            puntos += 1
            cola.append([None])
            print(puntos)

    else: # muere y pasa a la siguiente
        pts.append(puntos)
        print("- F")
        if(ia<poblacion):
            ia += 1
            
        if(ia == poblacion):
            ia = 0
            generacion += 1
            print("------------------- GENERACION {} -------------------".format(generacion))
            mx = 0
            mP = pts[0]
            change = True
            for i in range(1, poblacion):
                if(pts[i] > mP):
                    mx = i
                    mP = pts[i]
                if(i<poblacion-1 and pts[i] != pts[i+1]):
                    change = False

            if(change):
                padre = nns[mx]
                nns = [padre]
                for i in range(poblacion-1):
                    nns.append(createNnH(topology, sigm, padre, er))
            else:
                for i in range(poblacion):
                    nns.append(createNnP(topology, sigm))

            pts = []
        vel = [0,0]
        puntos = 0
        cola = []
        for i in range(3):
            cola.append([-1*(i-1)*15, 15])
        perder = False
        posCom = creaCom()
            
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    
    if not perder: 
        pantalla.fill(NEGRO)
        bordes()
        if puntos < 10:
            fuente = pygame.font.Font(None, 500)
            txt = fuente.render(str(puntos), True, (50, 50, 50))
            pantalla.blit(txt, [300,200])
        elif puntos <100:
            fuente = pygame.font.Font(None, 500)
            txt = fuente.render(str(puntos), True, (50, 50, 50))
            pantalla.blit(txt, [175,200])
            
        pygame.draw.rect(pantalla, ROJO, [posCom[0]+1, posCom[1]+1, 13, 13])
            
        for x in cola:
            if x != [None]:
                if 15 <= x[0] :
                    pygame.draw.rect(pantalla, VERDE, [x[0]+1, x[1]+1, 13, 13])


        
    pygame.display.flip()
    reloj.tick(480)

pygame.quit()
