import pygame
import random

class Color:
    def __init__(self, id, c):
        self.id = id
        self.c = c
        self.cat = 0

def compruebaInicio(cols):
    cols[0][0].cat = 1
    for i in range(n):
        for j in range(n):
            if(cols[i][j].cat == 1):
                if(i<n-1 and cols[i][j].id == cols[i+1][j].id and 
                    cols[i+1][j].cat == 0): # une los del mismo color
                    cols[i+1][j].cat = 1

                if(j<n-1 and cols[i][j].id == cols[i][j+1].id and
                    cols[i][j+1].cat == 0):
                    cols[i][j+1].cat = 1

                if(i>0 and cols[i][j].id == cols[i-1][j].id and 
                    cols[i-1][j].cat == 0): 
                    cols[i-1][j].cat = 1

                if(j>0 and cols[i][j].id == cols[i][j-1].id and
                    cols[i][j-1].cat == 0):
                    cols[i][j-1].cat = 1


NEGRO = (0, 0 ,0)

listaC = [(0, 255, 0),
          (255, 0, 0),
          (0, 0, 255), 
          (98, 0, 255),
          (237, 117, 47)]


res = 50
n = 15
dimensiones = [n*res, n*res]

cols = []
for i in range(n):
    cols.append([])
    for j in range(n):
        r = random.randrange(0, len(listaC))
        cols[i].append(Color(r, listaC[r]))

punt = 0
compruebaInicio(cols)
cambio = False
fin = False
anim = 0


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Flood")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

        if evento.type == pygame.MOUSEBUTTONDOWN:
            cambio = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------

    if(fin):
        for i in range(n):
            r = random.randrange(0, len(listaC))
            cols[i][anim] = Color(r, listaC[r])
        anim += 1

        if(anim == n):
            '''
            for i in range(n):
                for j in range(n):
                    r = random.randrange(0, len(listaC))
                    cols[i][j] = Color(r, listaC[r])
            '''
            compruebaInicio(cols)
            print(punt)
            punt = 0
            cols[0][0].cat = 1
            cambio = False
            fin = False
            anim = 0

    if(cambio):
        punt += 1
        p = pygame.mouse.get_pos()
        x = p[0]
        y = p[1]
        xi = int(x/res)
        yi = int(y/res)

        for i in range(n):
            for j in range(n):

                if(cols[i][j].cat == 1):
                    cols[i][j].c = cols[xi][yi].c # cambia el color del flood
                    cols[i][j].id = cols[xi][yi].id

            
                    if(i<n-1 and cols[i][j].id == cols[i+1][j].id and 
                        cols[i+1][j].cat == 0): # une los del mismo color
                        cols[i+1][j].cat = 1

                    if(j<n-1 and cols[i][j].id == cols[i][j+1].id and
                        cols[i][j+1].cat == 0):
                        cols[i][j+1].cat = 1

                    if(i>0 and cols[i][j].id == cols[i-1][j].id and 
                        cols[i-1][j].cat == 0): 
                        cols[i-1][j].cat = 1

                    if(j>0 and cols[i][j].id == cols[i][j-1].id and
                        cols[i][j-1].cat == 0):
                        cols[i][j-1].cat = 1

        for i in range(n):  # segunda revision porque en la primera se puede dejar alguno
            for j in range(n):

                if(cols[i][j].cat == 1):
                
                    if(i<n-1 and cols[i][j].id == cols[i+1][j].id and 
                        cols[i+1][j].cat == 0): # une los del mismo color
                        cols[i+1][j].cat = 1

                    if(j<n-1 and cols[i][j].id == cols[i][j+1].id and
                        cols[i][j+1].cat == 0):
                        cols[i][j+1].cat = 1

                    if(i>0 and cols[i][j].id == cols[i-1][j].id and 
                        cols[i-1][j].cat == 0): # une los del mismo color
                        cols[i-1][j].cat = 1

                    if(j>0 and cols[i][j].id == cols[i][j-1].id and
                        cols[i][j-1].cat == 0):
                        cols[i][j-1].cat = 1
        cambio = False

        fin = True
        for i in range(n):
            for j in range(n):
                if(cols[i][j].cat == 0):
                    fin = False
                    break
                    


    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)

    for i in range(n):
        for j in range(n):
            pygame.draw.rect(pantalla, cols[i][j].c, [i*res, j* res, res, res])

    for i in range(n):
        for j in range(n):
            if(i<n-1 and cols[i][j].id != cols[i+1][j].id):
                pygame.draw.line(pantalla, NEGRO, [i*res+res, j* res], [i*res+res, j* res+res], 2)

            if(j<n-1 and cols[i][j].id != cols[i][j+1].id):
                pygame.draw.line(pantalla, NEGRO, [i*res, j*res+res], [i*res+res, j* res+res], 2)


    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
