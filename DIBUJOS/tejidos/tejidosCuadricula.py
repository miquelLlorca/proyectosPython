import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


class Tejido:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dim = [len(x), len(y)]
    

    def Draw(self, pantalla, escala):
        
        step = 0

        for i in range(self.dim[0]): # se recorren las x y se dibujan las lineas
            step = self.x[i]
            for j in range(self.dim[1]):
                if(step == 1):
                    pygame.draw.line(pantalla, NEGRO, [i*escala, j*escala], [i*escala, (j+1)*escala], 3)
                    step = 0
                else:
                    step = 1

        
        for i in range(self.dim[1]): # se recorren las x y se dibujan las lineas
            step = self.y[i]
            for j in range(self.dim[0]):
                if(step == 1):
                    pygame.draw.line(pantalla, NEGRO, [j*escala, i*escala], [(j+1)*escala, i*escala], 3)
                    step = 0
                else:
                    step = 1








# ===================================================================================================================

def GeneraTejidoRandom(x, y, prob): # prob es la probabilidad de que sea 1
    X = []
    Y = []

    for i in range(x):
        if(random.random() <= prob):
            X.append(1)
        else:
            X.append(0)

    for i in range(y):
        if(random.random() <= prob):
            Y.append(1)
        else:
            Y.append(0)

    return Tejido(X, Y)

# ===================================================================================================================

x = 50
y = 30
prob = 0.45343
tejido = GeneraTejidoRandom(x, y, prob)

escala = 25
dimensiones = [x*escala for x in tejido.dim]


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Tejido")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                tejido = GeneraTejidoRandom(x, y, prob)
    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((100, 100, 100))

    tejido.Draw(pantalla, escala)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
