import pygame
import random
from gCode import creaGcode

# ------------------------------------------------------------STRUCTS ----------------------------------------------

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


class Circulo():
    def __init__(self, c, r):
        self.c = c
        self.r = r
    def __str__(self):
        cad = ""
        cad = cad + "(" + str(self.c[0]) + ", " + str(self.c[1]) + ")"
        cad = cad + " - "
        cad = cad + "(" + str(self.r) + ")"
        return cad

# ------------------------------------------------------------FUNCIONES ----------------------------------------------


    
# ---------------------------------------------------------------- MAIN -----------------------------------------------
def cuadricula():
    NEGRO = (0, 0 ,0)
    BLANCO = (255, 255, 255)
    VERDE = (0, 255, 0)
    ROJO = (255, 0, 0)

    lineas = []
    circulos = []
    res = 50
    pintar = False
    circ = False
    fincirc = False
    p0 = []

    pygame.init()
    dimensiones = [700,500]
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Cuadricula")
    hecho = False
    reloj = pygame.time.Clock()

    # Ocultamos el cursor del ratón.
    pygame.mouse.set_visible(0)

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                fincirc = not fincirc
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pintar = not pintar
                    if(not pintar):
                        p0 = []
                if evento.key == pygame.K_z:
                    if(circ):
                        if(len(circulos)>0):
                            circulos.pop(len(circulos)-1)
                    else:
                        if(len(lineas)>0):
                            lineas.pop(len(lineas)-1)
                        
                if evento.key == pygame.K_c:
                    circ = not circ
                        
        # ---------------------------------------------------LÓGICA---------------------------------------------------

        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        
        if(pintar):
            if(circ): # circulos
                xi = int(x/res)
                yi = int(y/res)

                for i in range(xi-1, xi+1):
                    for j in range(yi-1, yi+1):
                        dx = abs(x - i*res)
                        dy = abs(y - j*res)
                        if(dx < 10 and dy < 10): # seleccion punto
                            if(fincirc):
                                circulos.append(Circulo(p0, dc))
                                fincirc = False
                                p0 = []
                            elif(p0 == []):
                                p0 = (i*res, j*res)
                            break

            else: # lineas
                xi = int(x/res)
                yi = int(y/res)

                for i in range(xi-1, xi+1):
                    for j in range(yi-1, yi+1):
                        dx = abs(x - i*res)
                        dy = abs(y - j*res)
                        if(dx < 10 and dy < 10): # seleccion punto
                            if(p0 != []) and (p0[0] != i*res or p0[1] != j*res):
                                lineas.append(Linea(p0, (i*res, j*res)))
                            
                            p0 = (i*res, j*res)
                            break
                
        # ---------------------------------------------------DIBUJO---------------------------------------------------

        pantalla.fill(BLANCO)

        # cuadricula
        for i in range(int(dimensiones[0]/res)):
            pygame.draw.line(pantalla, (50, 50, 50), [i*res, 0], [i*res, dimensiones[1]], 1)
            
        for i in range(int(dimensiones[1]/res)):
            pygame.draw.line(pantalla, (50, 50, 50), [0, i*res], [dimensiones[0], i*res], 1)

        # dibujo
        for L in lineas: 
            pygame.draw.line(pantalla, NEGRO, L.x, L.y, 4) # lineas 

        for C in circulos:
            pygame.draw.ellipse(pantalla, NEGRO, [C.c[0] - C.r +1, C.c[1] - C.r +1, C.r*2, C.r*2], 4) # circulos

        # cursor
        if(pintar):
            pygame.draw.ellipse(pantalla, VERDE, [x-5, y-5, 10, 10])
        else:
            pygame.draw.ellipse(pantalla, ROJO, [x-5, y-5, 10, 10])
        pygame.draw.ellipse(pantalla, NEGRO, [x-6, y-6, 12, 12], 1)

        # progreso dibujo
        if(p0 != [] and circ):
            dc = ((p0[0]-x)**2 + (p0[1]-y)**2)**0.5
            if(dc>5):
                pygame.draw.ellipse(pantalla, (50, 50, 50), [p0[0]-dc+1, p0[1]-dc+1, dc*2, dc*2], 2)
        elif(p0 != [] and not circ):
            pygame.draw.line(pantalla, (50, 50, 50), p0, pos, 2)
         


        
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

    sn = input("Guardar? [s/n]  ")

    if(sn == 's' or sn == 'S'):
        creaGcode(lineas, circulos)
        

