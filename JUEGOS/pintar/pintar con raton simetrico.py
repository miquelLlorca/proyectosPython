import pygame
import numpy as np


NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
GRIS = (150, 150, 150)

dimensiones = [1000, 1000]
centro = [int(d/2) for d in dimensiones]


# ================================================================================================================================

# polar = [distancia, angulo]
# cart  = [x, y] 

def PolarToCartesian(coord):
    newCoord = [0, 0]
    newCoord[0] = int(coord[0] * np.cos(np.radians(coord[1])))
    newCoord[1] = int(coord[0] * np.sin(np.radians(coord[1])))
    return newCoord


def CartesianToPolar(coord):
    newCoord = [0, 0]
    newCoord[0] = np.sqrt(coord[0]**2 + coord[1]**2)
    newCoord[1] = np.degrees(np.arctan(coord[1]/coord[0])) if coord[0] != 0 else 90
    return newCoord

xy = [1,100]
polar = CartesianToPolar(xy)
print(xy)
print(polar)
print(PolarToCartesian(polar))

# xy [123, 456]
# xy a polar [472.2975756871932, 1.3073297857599793]
# polar a xy [472.17463605033726, 10.775577512668315]


def GetSimetricos(centro, n, polar):
    radios = []

    step = 360/n
    for i in range(n):
        conv = PolarToCartesian(polar)
        radios.append(conv)

        polar[1] += step

    return radios

def GetRadios(centro, n):
    polar = [1000, 0]
    radios = GetSimetricos(centro, n, polar)
    radios = [[r[i] + centro[i] for i in range(2)] for r in radios]
    return radios

# ================================================================================================================================

class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Imagen:
    def __init__(self):
        self.pixeles = []

    def Paint(self, pos, color):
        if(pos not in self.pixeles ):
            self.pixeles.append(Pixel(pos[0], pos[1], color))
            
            for pix in GetSimetricos(centro, n, CartesianToPolar(pos)):
                self.pixeles.append(Pixel(pix[0], pix[1], color))


    def Draw(self, pantalla):
        for pix in self.pixeles:
            pygame.draw.rect(pantalla, pix.color, [pix.x, pix.y, 1, 1])


# ================================================================================================================================

color = NEGRO
n = 6 # numero de radios de simetria
paint = False

radios = GetRadios(centro, n)
imagen = Imagen()



pygame.init()
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption('Pintar simetrico')
hecho = False
reloj = pygame.time.Clock()
pos = pygame.mouse.get_pos()
pygame.mouse.set_visible(0)

while not hecho:
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True  
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                color = NEGRO
            if evento.key == pygame.K_2:
                color = ROJO
            if evento.key == pygame.K_3:
                color = AZUL
            if evento.key == pygame.K_4:
                color = VERDE
            if evento.key == pygame.K_5:
                color = VIOLETA
   

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            paint = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            paint = False
            
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    pos = pygame.mouse.get_pos()

    if(paint):
        imagen.Paint(pos, color)

        

    # ---------------------------------------------------DIBUJO---------------------------------------------------
    pantalla.fill(BLANCO)
    # dibuja ejes
    for i in range(n):
        pygame.draw.line(pantalla, GRIS, centro, radios[i], 1)
    # dibuja dibujo
    imagen.Draw(pantalla)

    # dibuja raton
    pygame.draw.ellipse(pantalla, ROJO, [pos[0]-2, pos[1]-2, 4, 4])



    pygame.display.flip()
    reloj.tick(600)
    
pygame.quit()
