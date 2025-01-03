import pygame
import random
import numpy as np
import os
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
A = (247, 2, 35)
B = (94, 153, 247)
DIFF_C = [A[i]- B[i] for i in range(3)]


MASS_MULTIPLIER = 1
CONSTANTE_GRAVITATORIA = 100

def Normalize(v):
    mod = np.sqrt(v[0]**2 + v[1]**2)
    v = [x/mod for x in v]
    return v

def Multiply(v, m):
    return [x*m for x in v]

def GetColor(v, min, max):
    res = 50
    v -= min
    max -= min      # se pasa de 0 a (max-min)
    step = max/res  # se divide max entre la resolucion
    x = int((v/step if step!=0 else 0))
    color = [B[i]+DIFF_C[i]*x/res for i in range(3)]
    return color
# ========================================================================================

class Masa:
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m

    def GetDistanceVector(self, x, y):
        v = []
        v.append(self.x - x)
        v.append(self.y - y)
        return v

    def GetDistanceVectorNormalized(self, i, j, res):
        x = i*res + res/2
        y = j*res + res/2
        v = m.GetDistanceVector(x, y)
        mod = np.sqrt(v[0]**2 + v[1]**2)
        v = [x/mod for x in v]
        return v

    def GetDistance(self, x, y):
        v = m.GetDistanceVector(x, y)
        return np.sqrt(v[0]**2 + v[1]**2)

    def Draw(self, pantalla):
        pygame.draw.ellipse(pantalla, NEGRO, [self.x-5, self.y-5, 10, 10])

# ========================================================================================

class HeatMap:
    def __init__(self, tam, res):
        self.x = tam[0]
        self.y = tam[1]
        self.res = res
        self.valores = np.zeros(shape=tam)
        self.direcciones = np.zeros(shape=tam+[2])
        self.rangoV = [0,0]

    def CalculaMapa(self, masas):
        rango = [10000, -10000]
        for i in range(self.x):
            for j in range(self.y):
                for m in masas:
                    x = i*res + res/2
                    y = j*res + res/2
                    print(m.m)
                    self.valores[i][j] += CONSTANTE_GRAVITATORIA * m.m / m.GetDistance(x, y)# G * m / r**2
                    
                    v = m.GetDistanceVector(x, y)
                    self.direcciones[i][j][0] += v[0]
                    self.direcciones[i][j][1] += v[1]
                
                v = Normalize(self.direcciones[i][j])
                self.direcciones[i][j] = Multiply(v, res/2)

                if(self.valores[i][j] < rango[0]):
                    rango[0] = self.valores[i][j]
                if(self.valores[i][j] > rango[1]):
                    rango[1] = self.valores[i][j]

        self.rangoV = rango

        return

    def Draw(self, pantalla) -> None:

        for i in range(self.x):
            for j in range(self.y):
                c = GetColor(self.valores[i][j], self.rangoV[0], self.rangoV[1])
                pygame.draw.rect(pantalla, c, [i*self.res, j*self.res, res, res])


        for i in range(self.x):
            for j in range(self.y):
                x = i*res + res/2
                y = j*res + res/2
                pygame.draw.ellipse(pantalla, NEGRO, [x-1, y-1, 2, 2])
                pygame.draw.line(pantalla, NEGRO, [x,y], [x+self.direcciones[i][j][0],y+self.direcciones[i][j][1]])

        return
# ========================================================================================


# MAIN =================================================================================================================

if(__name__ == "__main__"):

    res = 20
    tam = [50, 50]
    dimensiones = [res*t for t in tam]

    masas = [
        Masa(x=230, y=160, m=5*MASS_MULTIPLIER),
        Masa(x=100, y=480, m=1*MASS_MULTIPLIER),
        Masa(x=460, y=280, m=2*MASS_MULTIPLIER)
    ]

    heatmap = HeatMap(tam, res)

    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Lagrange")
    hecho = False
    reloj = pygame.time.Clock()

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True
            
            if evento.type == pygame.KEYDOWN: 
                if evento.key == pygame.K_SPACE:
                    os.system("clear")
                    heatmap.CalculaMapa(masas)


        # LÓGICA---------------------------------------------LÓGICA---------------------------------------------LÓGICA
        pos = pygame.mouse.get_pos()
        # DIBUJO---------------------------------------------DIBUJO---------------------------------------------DIBUJO

        pantalla.fill(BLANCO)

        heatmap.Draw(pantalla)

        for m in masas:
            m.Draw(pantalla)


        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
