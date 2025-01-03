import pygame
import random

from color import *

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

ESCALA = 2

path = "/home/miquel/Downloads/Fondo-de-Ubuntu-22.04.png"
img = PixelArtImage(path)
img.LoadImage()
img.Resize((20,10))

tabl = Tablero()
tabl.DrawImage(img)
color = ColorPicker([100, 100])
click = False
pos = [0, 0]
v = [0, 0]
borrar  = False


pygame.init()
dimensiones = [1000, 1800]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Pixel art")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if evento.type == pygame.MOUSEBUTTONUP:
            click = False
            color.UnClick()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                v[0] = 1
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                v[0] = -1
            if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                v[1] = 1
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                v[1] = -1

            if evento.key == pygame.K_SPACE:
                borrar = not borrar

            if evento.key == pygame.K_PLUS:
                tabl.Escalar(1/ESCALA, dimensiones)
            if evento.key == pygame.K_MINUS:
                tabl.Escalar(ESCALA, dimensiones)

        if evento.type == pygame.KEYUP:
            v = [0, 0]

    # ---------------------------------------------------LÓGICA---------------------------------------------------

    prevPos = pos
    pos = pygame.mouse.get_pos()
    
    if(color.move):
        dP = [prevPos[0]-pos[0], prevPos[1]-pos[1]]
        color.Move(dP)

    if(click):
        if(not color.Click(pos)):
            if(not borrar):
                tabl.Pintar(pos, color.selected)
            else:
                tabl.Borrar(pos)
        

    tabl.Move(v)

    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    
    tabl.Draw(pantalla)
    color.Draw(pantalla)

    #fuente = pygame.font.Font(None, 75)
    #txt = fuente.render('GAME OVER', True, (0,0,0))
    #pantalla.blit(txt, [200,300])

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
