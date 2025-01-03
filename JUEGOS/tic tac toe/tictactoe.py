import pygame
import random

# CONST
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)


# CLASES

class Tablero:
    def __init__(self):
        self.tablero = []
        for i in range(3):
            self.tablero.append([])
            for j in range(3):
                self.tablero[i].append(0)

        self.turno = 0
        self.finished = False



    def Move(self, pos):
        if(not self.finished and self.tablero[pos[0]][pos[1]] == 0):
            self.tablero[pos[0]][pos[1]] = 1 + self.turno%2
            self.turno += 1

            if(self.turno == 9):
                self.finished = True


    



# MAIN

dimensiones = [900, 900]
res = int(dimensiones[0]/3)
tabl = Tablero()


pygame.init()

pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Tetris')
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                tabl = Tablero()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = [ int(x/res) for x in pygame.mouse.get_pos()]
            tabl.Move(pos)
            
        
    #----------------------------------------------LÓGICA----------------------------------------------
                


    #----------------------------------------------DIBUJO ----------------------------------------------

    pantalla.fill(NEGRO)
    
    

    pygame.draw.rect(pantalla, BLANCO, [res, -100, res, dimensiones[0]+200], 10)
    pygame.draw.rect(pantalla, BLANCO, [-100, res, dimensiones[0]+200, res], 10)

    for i in range(3):
        for j in range(3):
            if(tabl.tablero[i][j] == 1):
                pygame.draw.ellipse(pantalla, BLANCO, [i*res+20, j*res+20, res-40, res-40], 10)

            elif(tabl.tablero[i][j] == 2):
                pygame.draw.line(pantalla, BLANCO, [i*res+25, j*res+20], [(i+1)*res-30, (j+1)*res-20], 10)
                pygame.draw.line(pantalla, BLANCO, [i*res+25, (j+1)*res-20], [(i+1)*res-30, j*res+20], 10)




    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
