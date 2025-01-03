import pygame
from random import randrange

NEGRO = (0, 0 ,0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)








class Snake:
    def __init__(self, dimensiones):
        self.cola = []
        for i in range(3):
            self.cola.append([-1*(i-1)*15, 15])
        
        self.dimensiones = dimensiones
        self.posCom = self.CreaComida()
        self.puntos = 0
        self.orientacion = 0


    def creaComida(self):
        return [randrange(10,self.dimensiones[0]-10), randrange(10,self.dimensiones[1]-10)]

    def Girar(self, dir):
        self.orientacion += dir * 1 # hay que austar esto, 1 probablemete sea poco

    def Mover(self):
        self.cola

# ==================================================================================



serpiente = Snake()

perder = False
fps = 10
dimensiones = [1000, 1000]


pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Snake')
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                serpiente.Girar(-1)
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                serpiente.Girar(1)

            if evento.key == pygame.K_r: #reset
                vel = [0,0]
                puntos = 0
                cola = []
                for i in range(3):
                    cola.append([-1*(i-1)*15, 15])
                perder = False
                posCom = creaCom()

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    
            
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    
   
    pantalla.fill(NEGRO)
    
    if puntos < 10:
        fuente = pygame.font.Font(None, 500)
        txt = fuente.render(str(puntos), True, (50, 50, 50))
        pantalla.blit(txt, [300,200])
    elif puntos <100:
        fuente = pygame.font.Font(None, 500)
        txt = fuente.render(str(puntos), True, (50, 50, 50))
        pantalla.blit(txt, [175,200])
        
    pygame.draw.rect(pantalla, ROJO, [posCom[0]+1, posCom[1]+1, 13, 13])
        
    for x in serpiente.cola:
        pygame.draw.ellipse(pantalla, VERDE, [x[0]+1, x[1]+1, 13, 13])

 
        
    pygame.display.flip()
    reloj.tick(fps)

pygame.quit()
