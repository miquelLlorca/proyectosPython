import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


class Recta:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.puntos = []
        self.dir = [b[0]-a[0], b[1]-a[1]]

        for i in range(n):
            self.puntos.append([self.a[0]+i*self.dir[0]/n, self.a[1]+i*self.dir[1]/n])
        self.puntos.append(b)


dimensiones = [1000, 1000]

n = 50
origen = [100, 900]
l = 800
p = [origen[0]+l, origen[1]]
R1 = Recta(origen, p, n) 
p = [origen[0], origen[1]-800]
R2 = Recta(p, origen, n) 



pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Curvas")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_MINUS:
                n = n - 5
                origen = [100, 900]
                l = 800
                p = [origen[0]+l, origen[1]]
                R1 = Recta(origen, p, n) 
                p = [origen[0], origen[1]-800]
                R2 = Recta(p, origen, n)

            if evento.key == pygame.K_PLUS:
                n = n + 5
                origen = [100, 900]
                l = 800
                p = [origen[0]+l, origen[1]]
                R1 = Recta(origen, p, n) 
                p = [origen[0], origen[1]-800]
                R2 = Recta(p, origen, n)
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    pos = pygame.mouse.get_pos()
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((200, 200, 200))

    pygame.draw.line(pantalla, NEGRO, R1.a, R1.b, 3)
    pygame.draw.line(pantalla, NEGRO, R2.a, R2.b, 3)

    for i in range(1, n):        
        pygame.draw.line(pantalla, NEGRO, R1.puntos[i], R2.puntos[i], 1)


    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
