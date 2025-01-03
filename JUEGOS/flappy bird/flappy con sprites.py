import pygame
from random import randrange

class Bloque(pygame.sprite.Sprite):
    
    def __init__(self, color, largo, alto):         
        super().__init__()

        if color[0] == 'imagen':
            self.image = pygame.image.load("flappydef.png").convert()
            self.image.set_colorkey(BLANCO)
        elif color[0] == 'nada':
            self.image = pygame.Surface([largo, alto])
            self.image.fill(BLANCO)
            self.image.set_colorkey(BLANCO)
        else:
            self.image = pygame.Surface([largo+1, alto+2])
            self.image.fill(BLANCO)
            self.image.set_colorkey(BLANCO)
            if color[0] == 't1':
                pygame.draw.rect(self.image, color[1], [0, 0, largo, alto])
                pygame.draw.rect(self.image, NEGRO, [0,-2, largo, alto+1], 2)
            else:
                pygame.draw.rect(self.image, color[1], [0, 0, largo, alto])
                pygame.draw.rect(self.image, NEGRO, [0,0, largo, alto+2], 2)
        self.rect = self.image.get_rect()

    def update(self, v):
        self.rect.x -= v
        
    def updateprota(self, v):
        if self.rect.y + v[1] > 0:
            self.rect.y += v[1]
    
def altura(n):
    m = randrange(50, 350)
    while abs(n-m) > 200:
        m = randrange(50, 350)
    return m
        
pygame.init()
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
CIELO = (86, 148, 210)
TUBOS = (22, 195, 22)
SUELO = (64, 29, 29)

pos = [50, 200]
vel = [0, 0]
posTubos = []
for i in range(6):
    posTubos.append(500 + 150*i)

n = 200
allSprites = pygame.sprite.Group()
spriteTubos = pygame.sprite.Group()
v = 2.5
for i in range(6):
    n = altura(n)
    tubo = Bloque(['t1', TUBOS], 35, n)
    tubo.rect.x = 500+150*i
    tubo.rect.y = 0
    spriteTubos.add(tubo)
    allSprites.add(tubo)
    tubo = Bloque(['t2', TUBOS], 35, 500 - n - 90)
    tubo.rect.x = 500+150*i
    tubo.rect.y = n + 90
    spriteTubos.add(tubo)
    allSprites.add(tubo)
    
perder = False
colFinal = Bloque(['col', NEGRO], 150, 500)
colFinal.rect.x = -200
colFinal.rect.y = 0

colSuelo = Bloque(['nada', NEGRO],400, 30)
colSuelo.rect.x = 0
colSuelo.rect.y = 470
allSprites.add(colSuelo)

posF1 = [0,0]
posF2 = [400,0]

dimensiones = [400,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()

fondo = pygame.image.load("fondo.png").convert()
prota = Bloque(['imagen', 'a'], 20, 20)
prota.rect.x = pos[0]
prota.rect.y = pos[1]
PROTA = pygame.sprite.Group()
PROTA.add(prota)

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                vel[1] = -8
            if evento.key == pygame.K_r:
                pos = [50, 200]
                vel = [0, 0]
                posTubos = []
                for i in range(6):
                    posTubos.append(500 + 150*i)

                n = 200
                allSprites = pygame.sprite.Group()
                spriteTubos = pygame.sprite.Group()
                v = 2.5
                for i in range(6):
                    n = altura(n)
                    tubo = Bloque(['t1', TUBOS], 35, n)
                    tubo.rect.x = 500+150*i
                    tubo.rect.y = 0
                    spriteTubos.add(tubo)
                    allSprites.add(tubo)
                    tubo = Bloque(['t2', TUBOS], 35, 500 - n - 90)
                    tubo.rect.x = 500+150*i
                    tubo.rect.y = n + 90
                    spriteTubos.add(tubo)
                    allSprites.add(tubo)
                    
                perder = False
                colFinal = Bloque(['col', NEGRO], 35, 500)
                colFinal.rect.x = -100
                colFinal.rect.y = 0
                colSuelo = Bloque(['nada', NEGRO],400, 30)
                colSuelo.rect.x = 0
                colSuelo.rect.y = 470
                allSprites.add(colSuelo)
                prota = Bloque(['imagen', 'a'], 20, 20)
                prota.rect.x = pos[0]
                prota.rect.y = pos[1]
                PROTA = pygame.sprite.Group()
                PROTA.add(prota)
                posF1 = [0,0]
                posF2 = [400,0]

    # ---------------------------------------------------LÓGICA---------------------------------------------------
    spriteTubos.update(v)
    for i in range(6):
        posTubos[i] -= v

    elim = pygame.sprite.spritecollide(colFinal, spriteTubos, True)
    pygame.sprite.spritecollide(colFinal, allSprites, True)
    
    
    if elim != []:
        posTubos.pop(0)
        posTubos.append(posTubos[4]+150)
        elim = []
        n = altura(n)
        tubo = Bloque(['t1', TUBOS], 35, n)
        tubo.rect.x = posTubos[5]
        tubo.rect.y = 0
        spriteTubos.add(tubo)
        tubo = Bloque(['t2', TUBOS], 35, 500 - n - 90)
        tubo.rect.x = posTubos[5]
        tubo.rect.y = n + 90
        spriteTubos.add(tubo)

    vel[1] += 0.5
    elim2 = pygame.sprite.spritecollide(prota, allSprites,False)
    if elim2 != []:
        elim2 = []
        perder = True
    else:
        prota.updateprota(vel)

    posF1[0] -= 1
    posF2[0] -= 1
    # ---------------------------------------------------DIBUJO---------------------------------------------------
    pantalla.fill(CIELO)
    if not perder:
        pantalla.blit(fondo, posF1)
        pantalla.blit(fondo, posF2)
        PROTA.draw(pantalla)
        spriteTubos.draw(pantalla)
    else:
    
        fuente = pygame.font.Font(None, 50)
        txt = fuente.render('GAME OVER', True, (0,0,0))
        txt2 = fuente.render('Press R to restart', True, (0,0,0))
        pantalla.blit(txt, [100,200])
        pantalla.blit(txt2, [65, 235])
        
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
