import pygame

def esPrimo(x):
    if x != 1:
        for i in range(2, int(round(x**0.5 + 1, 0))):
            if x % i == 0:
                return 0
        return x
    return 0
    
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
dimensiones = [300, 600]
mat = []
x = int(dimensiones[0]/10)
y = int(dimensiones[1]/10)

for i in range(y):
    mat.append([])
    if len(mat) == 1:
        for j in range(1, x+ 1):
            mat[0].append(j + 1200)
    else:
        for j in range(1, x + 1):
            mat[i].append(j + mat[i-1][x - 1])

print(mat)

for i in range(y):
    for j in range(x):
        mat[i][j] = esPrimo(mat[i][j])



pygame.init()
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption('Numeros primos')
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill(NEGRO)
    for i in range(y):
        for j in range(x):
            if mat[i][j] != 0:
                pygame.draw.rect(pantalla, ROJO, [10*j+0.5, 10*i+0.5, 9, 9])
    pygame.display.flip()
    reloj.tick(1)

pygame.quit()
