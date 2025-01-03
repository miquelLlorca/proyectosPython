import pygame
from random import randrange
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  

class Piano:
    def __init__(self, dimensiones):
        self.dimensiones = dimensiones+[]
        self.ancho = int(dimensiones[0]/4)
        self.alto = self.ancho*2
        self.n = 6
        self.line = 800

        self.teclas = []
        for i in range(self.n):
            self.teclas.append(randrange(0, 4))


    def Press(self, n):
        if(n == self.teclas[1]):
            self.teclas.pop(0)
            self.teclas.append(randrange(0, 4))
        return


    def Draw(self, pantalla):
        
        pygame.draw.line(pantalla, ROJO, [0, self.line-self.alto/2], [self.dimensiones[0], self.line-self.alto/2], 2)
        
        x0 = self.line - self.alto*(self.n-1)
        for i in range(self.n):
            if(i == self.n-1):
                color = (100, 100, 100)
            else:
                color = NEGRO
            pygame.draw.rect(pantalla, color, [self.teclas[self.n-1-i]*self.ancho, x0+self.alto*i, self.ancho, self.alto-1])
            

        for i in range(3):
            pygame.draw.line(pantalla, NEGRO, [(i+1)*self.ancho, 0], [(i+1)*self.ancho, self.dimensiones[1]], 2)



dimensiones = [120*4, 1000]

p = Piano(dimensiones)


pygame.init()

pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Piano tiles")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_v:
                p.Press(0)
            if evento.key == pygame.K_b:
                p.Press(1)
            if evento.key == pygame.K_n:
                p.Press(2)
            if evento.key == pygame.K_m:
                p.Press(3)

    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    p.Draw(pantalla)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
