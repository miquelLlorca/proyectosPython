import pygame
from random import choice

class Puerta():
    def __init__(self, abierta, premio, x, y, a, h):
        self.abierta = abierta
        self.premio = premio
        self.x = x
        self.y = y
        self.alt = h
        self.anc = a
        
    def dibPuerta(self, imagen):
        if self.abierta:
            pygame.draw.rect(pantalla, (0,0,0), [self.x, self.y, self.anc, self.alt], 1)
            fuente = pygame.font.Font(None, 50)
            txt = fuente.render(self.premio , True, (0,0,0))
            pantalla.blit(txt, [self.x + self.anc//5, self.y + self.alt//2])
        else:
            im = pygame.image.load(imagen).convert()
            pantalla.blit(im, [self.x, self.y])
            

    
def elegirPremio():
    a = choice(('coche','cabra','cabra'))
    if a == 'coche':
        b = 'cabra'
        c = 'cabra'
    else:
            b = choice(('coche','cabra'))
            if b == 'coche':
                c = 'cabra'
            else:
                c = 'coche'
    return a, b, c

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

a, b, c = elegirPremio()
puerta1 = Puerta(False, a, 70, 50, 160, 300)
puerta2 = Puerta(False, b, 270, 50, 160, 300)
puerta3 = Puerta(False, c, 470, 50, 160, 300)
seleccion = Puerta(False, c, 0, 0, 0, 0)

pygame.init()
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Monty Hall')
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] <= 250:
                seleccion = puerta1
            elif 450 >= pos[0] > 250:
                seleccion = puerta2
            else:
                seleccion = puerta3
            
    # -----------------------------------LÓGICA-----------------------------------
    if not seleccion.abierta:
        seleccion.abierta=True
    # -----------------------------------DIBUJO-----------------------------------

    pantalla.fill(BLANCO)
    puerta1.dibPuerta('puerta1.png')
    puerta2.dibPuerta('puerta2.png')
    puerta3.dibPuerta('puerta3.png')
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
