from calculo_peso import calcPeso
import pygame

def datos(peso, p100):
    txt = fuente.render(peso[0], True, AZUL)
    pantalla.blit(txt, [390, 30])
    txt = fuente.render(peso[1], True, AZUL)
    pantalla.blit(txt, [345, 80])
    txt = fuente.render(p100, True, AZUL)
    pantalla.blit(txt, [610, 55])
    
def inputs():
    txt = fuente.render('1RM', True, NEGRO)
    pantalla.blit(txt, [70, 60])
    txt = fuente2.render('{', True, NEGRO)
    pantalla.blit(txt, [165, 30])
    
    txt = fuente.render('pectoral', True, NEGRO)
    pantalla.blit(txt, [200, 30])
    pygame.draw.rect(pantalla, NEGRO, [380, 70, 100, 2])
    
    txt = fuente.render('dorsal', True, NEGRO)
    pantalla.blit(txt, [200, 80])
    pygame.draw.rect(pantalla, NEGRO, [335, 120, 100, 2])
    
    txt = fuente.render('%', True, NEGRO)
    pantalla.blit(txt, [700, 60])
    pygame.draw.rect(pantalla, NEGRO, [600, 95, 100, 2])

def outputs(ejercicios, pesoDef):
    for i in range(len(ejercicios)):
        txt = fuente.render(ejercicios[i], True, NEGRO)
        pantalla.blit(txt, [70, 150 + 50*i])
        if pesoDef != []:
            txt = fuente.render(str(pesoDef[i]), True, AZUL)
            pantalla.blit(txt, [570, 150 + 50*i])

def seleccion(pos):
    if 335 < pos[0] < 480:
        if 20 < pos[1] < 70:
            return 'pectoral'
        elif 70 < pos[1] < 120:
            return 'dorsal'
    elif 600 < pos[0] < 700:
        if 45 < pos[1] < 95:
            return 'porcentaje'
    return None

def flecha(x, y, h, a):
    pygame.draw.line(pantalla, NEGRO, [x, y+(h/2)], [x+a, y+(h/2)], 2)
    pygame.draw.line(pantalla, NEGRO, [x+a, y+(h/2)], [x+(4*a/5), y], 2)
    pygame.draw.line(pantalla, NEGRO, [x+a, y+(h/2)], [x+(4*a/5), y+h], 2)

    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
ejercicios = ['Pectoral','Dorsal','Biceps','Sentadilla','Pectoral abierto',
              'Dorsal mancuerna','Triceps','Hombro']
peso = ['0', '0']
pesoDef = []
p100 = '0'
sel = None
esc = False

pygame.init()
dimensiones = [900,600]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 65)
fuente2 = pygame.font.Font(None, 130)

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            sel = seleccion(pos)
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                n = 1
                esc = True
            elif evento.key == pygame.K_2:
                n = 2
                esc = True
            elif evento.key == pygame.K_3:
                n = 3
                esc = True
            elif evento.key == pygame.K_4:
                n = 4
                esc = True
            elif evento.key == pygame.K_5:
                n = 5
                esc = True
            elif evento.key == pygame.K_6:
                n = 6
                esc = True
            elif evento.key == pygame.K_7:
                n = 7
                esc = True
            elif evento.key == pygame.K_8:
                n = 8
                esc = True
            elif evento.key == pygame.K_9:
                n = 9
                esc = True
            elif evento.key == pygame.K_0:
                n = 0
                esc = True
            elif evento.key == pygame.K_r:
                peso = ['0', '0']
                pesoDef = []
                p100 = '0'
                sel = None
                esc = False
            
    # ---------------------------------------------------LÓGICA---------------------------------------------------
    if int(peso[0]) > 0 and int(peso[1]) > 0 and 0 < int(p100) <= 100:
        pesoDef = calcPeso(int(peso[0]),int(peso[1]), int(p100))
    if esc:
        if sel == 'pectoral':
            if peso[0] == '0':
                peso[0] = str(n)
            else:
                peso[0] += str(n)
        elif sel == 'dorsal':
            if peso[1] == '0':
                peso[1] = str(n)
            else:
                peso[1] += str(n)
        elif sel == 'porcentaje':
            if p100 == '0':
                p100 = str(n)
            else:
                p100 += str(n)
        esc = False
    
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(BLANCO)
    inputs()
    datos(peso, p100)
    outputs(ejercicios, pesoDef)
    for i in range(len(ejercicios)):
        flecha(490, 155 + 50*i, 30, 65)
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
