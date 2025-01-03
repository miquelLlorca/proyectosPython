import pygame
import random
from gCode import creaGcode

class Linea():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        cad = ""
        cad = cad + "(" + str(self.x[0]) + ", " + str(self.x[1]) + ")"
        cad = cad + " -> "
        cad = cad + "(" + str(self.y[0]) + ", " + str(self.y[1]) + ")"
        return cad
    
def sinPlantilla(): 
    NEGRO = (0, 0 ,0)
    BLANCO = (255, 255, 255)
    VERDE = (0, 255, 0)
    ROJO = (255, 0, 0)
    AZUL = (0, 0, 255)
    VIOLETA = (98, 0, 255)

    lineas = []
    pintar = False
    p0 = []
    
    pygame.init()
    dimensiones = [700,500]
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Libre")
    hecho = False
    reloj = pygame.time.Clock()

    # Ocultamos el cursor del ratón.
    pygame.mouse.set_visible(0)
    
    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pintar = not pintar
                    if(not pintar):
                        p0 = []
                if evento.key == pygame.K_z:
                    if(len(lineas)>0):
                        lineas.pop(len(lineas)-1)
                        
        # ---------------------------------------------------LÓGICA---------------------------------------------------
        
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
            
        if(pintar):
            if(p0 != []):
                if(p0[0]!=pos[0] or p0[1]!=pos[1]):
                    lineas.append(Linea(p0, pos))
                p0 = (x, y)
            else:
                p0 = (x, y)
        # ---------------------------------------------------DIBUJO---------------------------------------------------

        pantalla.fill(BLANCO)
        
        for L in lineas: 
            pygame.draw.line(pantalla, NEGRO, L.x, L.y, 3) # lineas

        # cursor
        if(pintar):
            pygame.draw.ellipse(pantalla, VERDE, [x-5, y-5, 10, 10])
        else:
            pygame.draw.ellipse(pantalla, ROJO, [x-5, y-5, 10, 10])
        pygame.draw.ellipse(pantalla, NEGRO, [x-6, y-6, 12, 12], 1)

        
        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()

    sn = input("Guardar? [s/n]  ")
    circulos = []
    if(sn == 's' or sn == 'S'):
        creaGcode(lineas, circulos)
