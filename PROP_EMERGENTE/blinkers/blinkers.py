import pygame
from random import randrange
t = 80

class Bloque():
    
    def __init__(self, blink, x, y, c):         
        super().__init__()
        
        self.blink = blink
        self.x = x
        self.y = y
        self.c = c

    def dib(self):
        x = self.x
        y = self.y
        
        pygame.draw.polygon(pantalla, NEGRO, [[x+ 50, y ] , [x+ t , y+ 30], [x+ t, y+ 50], [x+ 50, y+ t] , 
                                               [x+ 30, y+ t], [x, y+ 50]  , [x , y+ 30] ,[x+ 30, y ] ])

        #marco luz
        pygame.draw.ellipse(pantalla, BLANCO, [x+20, y+20, 40, 40], 2) 
        #flechas
        pygame.draw.polygon(pantalla, BLANCO, [[x+t/2, y+2], [x+t/2+5, y+12], [x+ t/2-5,y+12]])
        pygame.draw.polygon(pantalla, BLANCO, [[x+2 ,y+t/2], [x+12, y+t/2+5], [x+12, y+t/2-5]])
        pygame.draw.polygon(pantalla, BLANCO, [[x+t/2,  y+t-3], [x+t/2+5, y+t-13], [x+t/2-5, y+t-13]])
        pygame.draw.polygon(pantalla, BLANCO, [[x+t-3,  y+t/2], [x+t-13, y+t/2+5], [x+t-13, y+t/2-5]])
        #blink
        pygame.draw.ellipse(pantalla, (0, self.c, 0), [bloques[i].x + 21, bloques[i].y+21, 38, 38])

    def updateBlk(self, x):
        if(self.blink >= 100):
            self.blink = 0
        else:
            if(x == 10):
                x = self.blink/10
            self.blink += x
            if(self.blink >= 100):
                return True
        return False
    
    def updateCol(self, blk):
        if(blk):
            self.c = 255
        elif(self.c > 5):
            self.c -= 25
        elif(self.c == 5):
            self.c = 0
            

        
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

sel = -1
moving = False
bloques = []

for i in range(6): # crear bloques
    b = Bloque(randrange(10, 90), 50 + 100*i, 50 + 100*i, 0)
    bloques.append(b)

pygame.init()
dimensiones = [700,700]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Comportamiento emergente")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            p0 = pygame.mouse.get_pos()
            x = p0[0]
            y = p0[1]
            sel = -1
            for i in range(len(bloques)):
                cx = bloques[i].x+30 <= x <= bloques[i].x + t-30
                cy = bloques[i].y+30 <= y <= bloques[i].y + t-30
                if(cx and cy):
                    sel = i
                    break
                
            moving = True
        if evento.type == pygame.MOUSEBUTTONUP:
            moving = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r: # resetear timers
                for i in range(len(bloques)):
                    bloques[i].blink = randrange(10, 90)
                    
    # ---------------------------------------------------LÓGICA---------------------------------------------------

    if(moving and sel!=-1):
        pos = pygame.mouse.get_pos()
        bloques[sel].x += pos[0] - p0[0]
        bloques[sel].y += pos[1] - p0[1]
        p0 = [pos[0], pos[1]]
        
        
    blks = []
    for i in range(len(bloques)): # actualiza timers  sin tener en cuenta al resto
        blks.append(bloques[i].updateBlk(1))

    act = []
    for i in range(len(bloques)): # actualiza timers segun lo que ve
        for j in range(len(bloques)):
            if(i!=j):
                cx = bloques[i].x <= bloques[j].x + t/2 <= bloques[i].x+t
                cy = bloques[i].y <= bloques[j].y + t/2 <= bloques[i].y+t
                if(blks[j] and (cx or cy)):
                    if(bloques[i].updateBlk(10)):
                        act.append(i)
                        
    for x in act:
        blks[x] = True
       
    for i in range(len(bloques)):
        bloques[i].updateCol(blks[i])
        
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    
    for i in range(len(bloques)): # dibuja bloques y blinks
        bloques[i].dib()

        
        
    pygame.display.flip()
    reloj.tick(50)

pygame.quit()
