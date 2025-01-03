import pygame
import time





def creaPos(x, y):
    return [[x, y], [x+100, y], [x+100, y+100], [x, y+200], [x, y+100], [x, y], [x, y+100]]


def numero(x):
    '''
        1
    6      2
        7
    5      3
        4
    '''
    if x == 0:
        return [True, True, True, True, True, True, False]
    if x == 1:
        return  [False, True, True, False, False, False, False]
    if x == 2:
        return  [True, True, False, True, True, False, True]
    if x == 3:
        return  [True, True, True, True, False, False, True]
    if x == 4:
        return  [False, True, True, False, False, True, True]
    if x == 5:
        return  [True, False, True, True, False, True, True]
    if x == 6:
        return  [True, False, True, True, True, True, True]
    if x == 7:
        return  [True, True, True, False, False, False, False]
    if x == 8:
        return  [True, True, True, True, True, True, True]
    if x == 9:
        return  [True, True, True, False, False, True, True]

def  printN(num, pos):
    for i in range(1,8):
        if num[i-1]:
            if i in [1, 4, 7]:
                drawSegment1(pos[i-1][0], pos[i-1][1])
            else:
                alto = 150
                ancho = 50
                drawSegment2(pos[i-1][0], pos[i-1][1])

def drawSegment1(x, y):
    dx = 60
    px = 0
    py = 1
    h = 50
    b = 150
    
    pygame.draw.rect(pantalla, VERDE, [x+dx, y, b-dx*2, h])
    
    pygame.draw.polygon(pantalla, VERDE, [[x, y+25], [x+dx, y], [x+dx, y+h]])
    
    pygame.draw.polygon(pantalla, VERDE, [[x+b, y+25], [x+(b-dx), y], [x+(b-dx), y+h]])



def drawSegment2(x, y):
    dy = 50
    px = 1
    py = 0
    h = 150
    b = 50
    
    pygame.draw.rect(pantalla, VERDE, [x, y+dy, b, h-dy*2])
    
    pygame.draw.polygon(pantalla, VERDE, [[x+25, y], [x, y+dy], [x+b, y+dy]])
    
    pygame.draw.polygon(pantalla, VERDE, [[x+25, y+h], [x, y+(h-dy)], [x+b, y+(h-dy)]])

    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

n = -1

pygame.init()
dimensiones = [1400,450]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Reloj')
hecho = False
reloj = pygame.time.Clock()
pantalla.fill(BLANCO)

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    

    
    seconds = time.time()# segundos desde epoch
    local_time = time.ctime(seconds)# tiempo local

    esp = 0
    hora = ''
    for c in local_time:
        if(c == ' '):
            esp+=1

        if(esp==3):
            if(c != ':' and c != ' '):
                hora += c
 
    # ---------------------------------------------------DIBUJO---------------------------------------------------
    pantalla.fill(NEGRO)
    
    x = 100
    for i in range(6):
        if(i == 1):
            x += 190
        elif(i == 2):
            x += 260
        elif(2< i < 4):
            x += 190
        elif(i == 4):
            x += 260
        elif(4< i < 6):
            x += 190

        num = numero(int(hora[i]))
        pos = creaPos(x, 100)
        printN(num, pos)

    pygame.draw.ellipse(pantalla, VERDE, [470, 150, 50, 50])
    pygame.draw.ellipse(pantalla, VERDE, [470, 250, 50, 50])

    pygame.draw.ellipse(pantalla, VERDE, [920, 150, 50, 50])
    pygame.draw.ellipse(pantalla, VERDE, [920, 250, 50, 50])
    
            
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
