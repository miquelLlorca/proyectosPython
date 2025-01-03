import pygame
from random import randrange
from os import system
tam = 50

class Bloque:
    
    def __init__(self, blink, x, y, c):          
        self.blink = blink
        self.x = x
        self.y = y
        self.c = c


    def Draw(self):
        x = self.x
        y = self.y
        
        pygame.draw.rect(pantalla, NEGRO, [x, y, tam, tam], 1)

        #marco luz
        pygame.draw.ellipse(pantalla, BLANCO, [x+5, y+5, tam-10, tam-10], 2) 
        
        #blink
        pygame.draw.ellipse(pantalla, (0, self.c, 0), [x+6, y+6, tam-12, tam-12])


    def UpdateBlink(self, x):
        if(self.blink >= 100):
            self.blink = 0
        else:
            if(x == 10):
                x = self.blink/10
            self.blink += x
            if(self.blink >= 100):
                return True
        return False

    
    def UpdateColor(self, blk):
        if(blk):
            self.c = 255
        elif(self.c > 5):
            self.c -= 10
        elif(self.c == 5):
            self.c = 0
            

        
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

dimensiones = [1000,1000]

bloques = []
#bloques[0].append( Bloque(randrange(1, 900), 0, 0, 0) )

for i in range(int(dimensiones[0]/tam)):
    bloques.append([])
    for j in range(int(dimensiones[1]/tam)):
        bloques[i].append( Bloque(randrange(1, 900), i*tam, j*tam, 0) )

pygame.init()

pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Comportamiento emergente")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r: # resetear timers
                for i in range(len(bloques)):
                    bloques[i].blink = randrange(10, 90)
                    
    # ---------------------------------------------------LÓGICA---------------------------------------------------
        
        
    blks = []
    for i in range(len(bloques)): # actualiza timers  sin tener en cuenta al resto
        blks.append([])
        for j in range(len(bloques[0])):
            blks[i].append(bloques[i][j].UpdateBlink(1))


    act = []
    for i in range(len(bloques)): # actualiza timers segun lo que ve
        for j in range(len(bloques[0])):

            for x in [i-1, i+1]:
                if(0 <= x < len(bloques) and blks[x][j]):
                    if(bloques[i][j].UpdateBlink(10)):
                        act.append([i, j])

            for y in [j-1, j+1]:
                if(0 <= y < len(bloques[0]) and blks[i][y]):
                    if(bloques[i][j].UpdateBlink(10)):
                        act.append([i, j])



    for p in act:
        blks[p[0]][p[1]] = True

       
    for i in range(len(bloques)):
        for j in range(len(bloques[0])):
            bloques[i][j].UpdateColor(blks[i][j])
        
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((150, 150, 150))
    
    for i in range(len(bloques)): # dibuja bloques y blinks
        for j in range(len(bloques[0])):
            bloques[i][j].Draw()

    
        
    pygame.display.flip()
    reloj.tick(1200)

pygame.quit()
