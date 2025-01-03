import pygame
import random
class Bloque(pygame.sprite.Sprite):
    
    def __init__(self, pers):         
        super().__init__()
        listaCactus = ['cactus1', 'cactus2', 'cactusDoble', 'cactusTriple', 'cactus4ple']
        if pers in listaCactus:
            cactus = pers + '.png'
            self.image = pygame.image.load(cactus).convert()
            self.image.set_colorkey(BLANCO)
        elif pers == 'dino':
            self.image = pygame.image.load("dino.png").convert()
            self.image.set_colorkey(BLANCO)
        elif pers == 'col':
            self.image = pygame.Surface([50, 500])
            self.image.fill(ROJO)
            pygame.draw.rect(self.image, ROJO, [0, 0, 50, 500])
        self.rect = self.image.get_rect()
        
    def update(self, v):
        self.rect.x -= v

    def updateDino(self, v):
        self.rect.y += v
    
    
pygame.init()
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("dinosaurio chrome")
hecho = False
reloj = pygame.time.Clock()

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

puntos = 0
allSprites = pygame.sprite.Group()
spriteCactus = pygame.sprite.Group()
v = 7
posCactus = []
listaCactus = ['cactus1', 'cactus2', 'cactusDoble', 'cactusTriple', 'cactus4ple']
for i in range(7):
    c = random.randrange(3)
    cactus = Bloque(listaCactus[c])
    pos = 500+500*i
    posCactus.append(pos)
    cactus.rect.x = pos
    if c == 1 or c == 2:
        cactus.rect.y = 415
    else:
        cactus.rect.y = 400
    spriteCactus.add(cactus)
    allSprites.add(cactus)

colFinal = Bloque('col')
colFinal.rect.x = -100
colFinal.rect.y = 0

prota = Bloque('dino')
prota.rect.x = 100
prota.rect.y = 405
allSprites.add(prota)
velProta = 0
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                if 400 < prota.rect.y:
                    velProta = -11.25
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    spriteCactus.update(v)
    for i in range(len(posCactus)):
        posCactus[i] -= v
        
    elim = pygame.sprite.spritecollide(colFinal, spriteCactus, True)
    pygame.sprite.spritecollide(colFinal, allSprites, True)

    if elim != []:
        puntos += 1
        n = posCactus[6]+500
        posCactus.append(n)
        posCactus.pop(0)
        elim = []
        if puntos < 10:
            x = 3
        else:
            x = 5
        c = random.randrange(x)
        cactus = Bloque(listaCactus[c])
        cactus.rect.x = posCactus[5]
        if c == 1 or c == 2:
            cactus.rect.y = 415
        else:
            cactus.rect.y = 400
        spriteCactus.add(cactus)
        allSprites.add(cactus)
        
    elim2 = pygame.sprite.spritecollide(prota, spriteCactus,False)
    
    if elim2 != []:
        elim2 = []
        perder = True
        color = ROJO
    else:
        if prota.rect.y + velProta <= 405 and velProta != 0:
            prota.updateDino(velProta)
        else:
            if 11 > 405 - prota.rect.y > 0:
                prota.updateDino(405 - prota.rect.y)
            velProta = 0
        velProta += 0.5
        color = BLANCO
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(color)
    pygame.draw.line(pantalla, (32.5, 32.5, 32.5), [0, 450], [700, 450])
    allSprites.draw(pantalla)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
