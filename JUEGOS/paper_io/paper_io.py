import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

SPEED_CONSTANT = 10
FPS = 60
MAX_SPEED = 50
BORDER_SIZE = 600

class Player:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.screen_pos = [x, y]
        self.vel = [0, 0]
        self.acc = [0, 0]

    def move(self, axis, value):
        self.acc[axis] = value
        self.vel = [(v if abs(v)<MAX_SPEED else MAX_SPEED) for v in self.vel]
        print(self.vel)
        
    def update(self, time_diff):
        self.vel = [self.vel[i] + self.acc[i]*time_diff*SPEED_CONSTANT for i in range(2)]
        self.pos = [self.pos[i] + self.vel[i]*time_diff*SPEED_CONSTANT for i in range(2)]
    
    def draw(self, pantalla):
        pygame.draw.circle(pantalla, NEGRO, self.screen_pos, 15)
# ========================================================================================

def draw_borders(pantalla, center):
    pygame.draw.line(pantalla, ROJO, [-BORDER_SIZE+center[0], -BORDER_SIZE+center[1]], [-BORDER_SIZE+center[0], +BORDER_SIZE+center[1]], 10)
    pygame.draw.line(pantalla, ROJO, [+BORDER_SIZE+center[0], +BORDER_SIZE+center[1]], [-BORDER_SIZE+center[0], +BORDER_SIZE+center[1]], 10)
    pygame.draw.line(pantalla, ROJO, [+BORDER_SIZE+center[0], +BORDER_SIZE+center[1]], [+BORDER_SIZE+center[0], -BORDER_SIZE+center[1]], 10)
    pygame.draw.line(pantalla, ROJO, [-BORDER_SIZE+center[0], -BORDER_SIZE+center[1]], [+BORDER_SIZE+center[0], -BORDER_SIZE+center[1]], 10)

# MAIN =================================================================================================================

if(__name__ == "__main__"):
    dimensiones = [800,800]
    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("PAPER.IO")
    exit = False
    reloj = pygame.time.Clock()


    player = Player(dimensiones[0]/2, dimensiones[1]/2)

    # pers = pygame.image.load('flappydef.png').convert()
    # pers.set_colorkey(BLANCO)


    while not exit:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                exit = True
            if evento.type == pygame.KEYDOWN:
                    
                if evento.key == pygame.K_w:
                    player.move(axis=1, value=-1)
                if evento.key == pygame.K_a:
                    player.move(axis=0, value=1)
                if evento.key == pygame.K_s:
                    player.move(axis=1, value=1)
                if evento.key == pygame.K_d:
                    player.move(axis=0, value=-1)

        # LÓGICA---------------------------------------------LÓGICA---------------------------------------------LÓGICA
        pos = pygame.mouse.get_pos()
        player.update(1/FPS)
        # DIBUJO---------------------------------------------DIBUJO---------------------------------------------DIBUJO

        pantalla.fill(BLANCO)
        draw_borders(pantalla, player.pos)
        player.draw(pantalla)
        # fuente = pygame.font.Font(None, 75)
        # txt = fuente.render('GAME OVER', True, (0,0,0))
        # pantalla.blit(txt, [200,300])

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()
