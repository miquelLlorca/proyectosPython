import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


class Led:
    def __init__(self):
        self.t = 0
        self.deriva = random.random()
        self.color = 250

    def Update(self):
        if(self.color > 0):
            self.color -= 10

        self.t += 1
        if(random.random() < self.deriva):
            self.t += 1

        if(self.t > 100):
            self.t = 0
            self.color = 250
            return True
        return False

class Placa:
    def __init__(self, x, y, escala):
        self.x = x
        self.y = y
        self.escala = escala
        self.leds = []

        for i in range(x):
            self.leds.append([])
            for j in range(y):
                self.leds[i].append(Led())


    def Draw(self, pantalla):
        for i in range(self.x):
            for j in range(self.y):
                self.leds[i][j].Update()
                pygame.draw.ellipse(pantalla, (0, self.leds[i][j].color, 0), [i*self.escala, j*self.escala, self.escala, self.escala])
                


x = 74
y = 41
escala = 25
placa = Placa(x, y, escala)
dimensiones = [x*escala, y*escala]



pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("LEDS")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)

    placa.Draw(pantalla)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
