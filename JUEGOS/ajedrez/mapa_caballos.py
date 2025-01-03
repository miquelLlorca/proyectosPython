import pygame
import random

# CONSTS
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


# FUNCIONES

def mueveCaballo(pos):
    ps = []

    for x in [-2, -1, 1, 2]:
        for y in [-2, -1, 1, 2]:
            if(abs(x) != abs(y)):
                ps.append( [pos[0]+x, pos[1]+y] )

    return ps



def mover(lista):
    newPs = []

    for p in lista:
        for newP in mueveCaballo(p):
            if(0 <= newP[0] < 8 and 0 <= newP[1] < 8):
                newPs.append(newP)

    for newP in newPs:
        if(newP not in lista):
            lista.append(newP)






# MAIN

cols = [NEGRO, BLANCO]
res = 100
dimensiones = [res*8, res*8]
posList = [ [0, 0] ]
pasos = [0]
finished = False


pygame.init()

pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Caballos")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                mover(posList)

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    
    if(not finished):
        if(len(posList) < 64):
            mover(posList)
            pasos[len(pasos)-1] += 1
        else:
            newP = posList[0]
            newP[0] += 1
            if(newP[0]==8):
                newP = [0, newP[1]+1]
            
            if(newP[1] == 8):
                finished = True

            posList = [newP]
            pasos.append(0)


    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)


    if(not finished):
        c = 0
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(pantalla, cols[c%2], [i*res, j*res, res, res])
                c += 1
            c += 1

        for p in posList:
            pygame.draw.ellipse(pantalla, NEGRO, [p[0]*res+15, p[1]*res+15, res-30, res-30], 5)
            pygame.draw.ellipse(pantalla, AMARILLO, [p[0]*res+20, p[1]*res+20, res-40, res-40], 5)

    else:
        for i in range(8):
            for j in range(8):
                if(pasos[i + j*8] == 4):
                    color = (0, 255, 0)
                elif(pasos[i + j*8] == 5):
                    color = (255, 255, 0)
                elif(pasos[i + j*8] == 6):
                    color = (255, 0, 0)

                pygame.draw.rect(pantalla, color, [i*res, j*res, res, res])




    pygame.display.flip()
    reloj.tick(60)

pygame.quit()



#newP = [0, 0]
#for n in pasos:
#    print(newP, "->", n)
#
#    newP[0] += 1
#    if(newP[0]==8):
#        newP = [0, newP[1]+1]
#    
#    if(newP[1] == 8):
#        break
#
#    posList = [newP]
#