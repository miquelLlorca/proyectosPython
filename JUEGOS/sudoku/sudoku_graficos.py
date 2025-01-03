import pygame

def sudoku(t):
    for i in range(10):
        if i%3 == 0:
            grosor = 5
        else:
            grosor = 2
        pygame.draw.line(pantalla, NEGRO, [t, t+t*i], [10*t, t+t*i], grosor)
        pygame.draw.line(pantalla, NEGRO, [t+t*i, t], [t+t*i,10*t], grosor)

def escribir(n, posicion, color):
    fuente = pygame.font.Font(None, 75)
    txt = fuente.render(str(n), True, color)
        
    if  str(n) == '1':
        pantalla.blit(txt, [60*posicion[0] +18, 60*posicion[1] +8])
    else:
        pantalla.blit(txt, [60*posicion[0] +17, 60*posicion[1] +8])

def ajustar(fila, pos):
    a = [0, 1, 2]
    b = [3, 4, 5]
    c = [6, 7, 8]
    if fila in a:
        filas = a
    elif fila in b:
        filas = b
    elif fila in c:
        filas = c

    if pos in a:
        cols = a
    elif pos in b:
        cols = b
    elif pos in c:
        cols = c

    return filas, cols

def buscar(n, s, fila, pos):
    if n in s[fila]:
        return True
    for i in range(9):
        if n == s[i][pos]:
            return True
    filas, cols = ajustar(fila, pos)
    for f in filas:
        for c in cols:
            if s[f][c] == n and f != fila and c != pos:
                return True
    return False
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
tamaño = 60
sud = [['5', '3', 0, 0, '7', 0, 0, 0, 0],
       ['6', 0, 0, '1', '9', '5', 0, 0, 0],
       [0, '9', '8', 0, 0, 0, 0, '6', 0],
       ['8', 0, 0, 0, '6', 0, 0, 0, '3'],
       ['4', 0, 0, '8', 0, '3', 0, 0, '1'],
       ['7', 0, 0, 0, '2', 0, 0, 0, '6'],
       [0, '6', 0, 0, 0, 0, '2', '8', 0],
       [0, 0, 0, '4', '1', '9', 0, 0, '5'],
       [0, 0, 0, 0, '8', 0, 0, '7', '9']]
pos = [0,0]
n = 0

pygame.init()
dimensiones = [11*tamaño, 11*tamaño]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("sudoku")
hecho = False
reloj = pygame.time.Clock()


while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            if not(p[0] < tamaño or p[0] > tamaño*10 or p[1] < tamaño or p[1] > tamaño*10):
                for i in range(2):
                    pos[i] = (p[i]//60)-1
            n = 0
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                n = 1
            elif evento.key == pygame.K_2:
                n = 2
            elif evento.key == pygame.K_3:
                n = 3
            elif evento.key == pygame.K_4:
                n = 4
            elif evento.key == pygame.K_5:
                n = 5
            elif evento.key == pygame.K_6:
                n = 6
            elif evento.key == pygame.K_7:
                n = 7
            elif evento.key == pygame.K_8:
                n = 8
            elif evento.key == pygame.K_9:
                n = 9
            
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    if sud[pos[0]][pos[1]] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        sud[pos[0]][pos[1]] = n

    '''for i in range(9):
        for j in range(9):
            if sud[i][j] == 0:
                break
            if i == 8 and j == 8:
                pantalla.fill((244,244,244))
                fuente = pygame.font.Font(None, 75)
                txt = fuente.render('Ganador', True, (0,0,0))
                pantalla.blit(txt, [100,300])'''
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    
    pantalla.fill((244,244,244))
    sudoku(tamaño)
    pygame.draw.rect(pantalla, ROJO, [(pos[0]+1)*60-4, (pos[1]+1)*60-4, 70, 70],7)
    for i in range(9):
        for j in range(9):
            if sud[i][j] != 0:
                if sud[i][j] == sud[pos[0]][pos[1]] or sud[i][j] == str(sud[pos[0]][pos[1]]):
                    sn = buscar(sud[pos[0]][pos[1]], sud, i, j)
                    if sn:
                        escribir(sud[i][j], [i+1, j+1], ROJO)
                    else:
                        escribir(sud[i][j], [i+1, j+1], VERDE)
                elif sud[i][j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    escribir(sud[i][j], [i+1, j+1], NEGRO)
                else:
                    escribir(sud[i][j], [i+1, j+1], AZUL)

    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
