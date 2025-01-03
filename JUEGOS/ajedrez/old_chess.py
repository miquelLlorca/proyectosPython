import pygame
tam = 125

class Pieza:
    def __init__(self, x, y, color, tipo):
        self.x = x
        self.y = y
        if(color): # Blanco
            self.filler = (255, 255, 255)
            self.bound = (0, 0, 0)
        else: # Negro
            self.filler = (0, 0, 0)
            self.bound = (255, 255, 255)

        self.tipo = tipo
        if(tipo == "peon"):
            self.vertices = [ [self.x + 0.5*tam, self.y + 0.3*tam] ,
                              [self.x + 0.2*tam, self.y + 0.8*tam] , 
                              [self.x + 0.8*tam, self.y + 0.8*tam] ]
        elif(tipo == "caballo"):
            self.vertices = [ [self.x + 0.5*tam, self.y + 0.1*tam] ,
                              [self.x + 0.1*tam, self.y + 0.3*tam] , 
                              [self.x + 0.1*tam, self.y + 0.9*tam] ,
                              [self.x + 0.7*tam, self.y + 0.9*tam] ,
                              [self.x + 0.4*tam, self.y + 0.3*tam] , 
                              [self.x + 0.9*tam, self.y + 0.3*tam]]
        elif(tipo == "alfil"):
            self.vertices = [ [self.x + 0.5*tam, self.y + 0.1*tam] ,
                              [self.x + 0.4*tam, self.y + 0.3*tam] , 
                              [self.x + 0.45*tam, self.y + 0.5*tam] ,
                              [self.x + 0.3*tam, self.y + 0.9*tam] ,
                              [self.x + 0.7*tam, self.y + 0.9*tam] ,
                              [self.x + 0.55*tam, self.y + 0.5*tam] ,
                              [self.x + 0.6*tam, self.y + 0.3*tam] ]
        elif(tipo == "torre"):
            self.vertices = [ [self.x + 0.5*tam, self.y + 0.3*tam] , # falta de aqui p'abajo
                              [self.x + 0.2*tam, self.y + 0.8*tam] , 
                              [self.x + 0.8*tam, self.y + 0.8*tam] ]
        elif(tipo == "rey"):
            self.vertices = [ [self.x + 0.5*tam, self.y + 0.3*tam] ,
                              [self.x + 0.2*tam, self.y + 0.8*tam] , 
                              [self.x + 0.8*tam, self.y + 0.8*tam] ]
        elif(tipo == "reina"):
            self.vertices = [ [self.x + 0.5*tam, self.y + 0.3*tam] ,
                              [self.x + 0.2*tam, self.y + 0.8*tam] , 
                              [self.x + 0.8*tam, self.y + 0.8*tam] ]
        

    def draw(self):
        pygame.draw.polygon(pantalla, self.filler, self.vertices)
        pygame.draw.polygon(pantalla, self.bound, self.vertices, 5)

class Tablero:
    def __init__(self):
        self.tablero = []
        for i in range(8):
            self.tablero.append([])
            for j in range(8):
                self.tablero[i].append(0)
        self.tablero[0][0] = Pieza(2*tam + 10, 10, 0, "alfil")
        self.tablero[0][1] = Pieza(3*tam + 10, 10, 1, "caballo")

    def draw(self):
        for i in range(8):
            for j in range(8):
                if(self.tablero[i][j] != 0):
                    self.tablero[i][j].draw()



def seleccion(pos, t):
    x = int((pos[0] - 2*t - 10)/t)
    y = int((pos[1] - 10)/t)
    print(x, y)
    if(pos[0] - 2*t <0 or x>7 or y<0 or y>7):
        return [-1, -1]
    return [x, y]



NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
MARRON = (121, 83, 0)



sel = [-1, -1]
pygame.init()
tablero = Tablero()

dimensiones = [20 + 12*tam, 20 + 8*tam]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("CHESS")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
            break
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            sel = seleccion(pos, tam)
           
    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------
    
    pantalla.fill((130, 130, 130))
    
    pygame.draw.rect(pantalla, MARRON, [2*tam, 0, tam*8 + 20, tam*8 + 20])
    
    for i in range(8): # tablero
        for j in range(8):
            if((i+j)%2==0):
                pygame.draw.rect(pantalla, BLANCO, [10+2*tam+i*tam, 10+j*tam, tam, tam])
            else:
                pygame.draw.rect(pantalla, NEGRO, [10+2*tam+i*tam, 10+j*tam, tam, tam])

    if(sel != [-1, -1]):# seleccion
        pygame.draw.line(pantalla, ROJO, [10+2*tam+sel[0]*tam, 10+sel[1]*tam],
                         [10+2*tam+(sel[0]+1)*tam, 10+(sel[1])*tam], 3)
        pygame.draw.line(pantalla, ROJO, [10+2*tam+sel[0]*tam, 10+sel[1]*tam],
                         [10+2*tam+(sel[0])*tam, 10+(sel[1]+1)*tam], 3)
        pygame.draw.line(pantalla, ROJO, [10+2*tam+(sel[0])*tam, 10+(sel[1]+1)*tam],
                         [10+2*tam+(sel[0]+1)*tam, 10+(sel[1]+1)*tam], 3)
        pygame.draw.line(pantalla, ROJO, [10+2*tam+(sel[0]+1)*tam, 10+(sel[1])*tam],
                         [10+2*tam+(sel[0]+1)*tam, 10+(sel[1]+1)*tam], 3) 
    
    tablero.draw()
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
