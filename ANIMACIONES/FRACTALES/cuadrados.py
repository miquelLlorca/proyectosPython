import pygame
import random
 
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

dim = [700,700]
cs = []
diag = dim[0]/2
t = dim[0]/2
cs.append([diag , t])



pygame.init()
pantalla = pygame.display.set_mode(dim) 
pygame.display.set_caption("Cuadrados")
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        if(evento.type == pygame.KEYDOWN):
            if(evento.key == pygame.K_KP_PLUS):
                diag /= 2
                t  /= 2
                for i in range(int(dim[0]/diag)):
                    found = False
                    for j in range(len(cs)):
                        if(abs(diag*(i+1)-cs[j][0]) < 0.5):
                            found = True

                    if(not found):
                        cs.append([diag*(i+1), t])
    # ---------------------------------------------------LÓGICA---------------------------------------------------
  
    # ---------------------------------------------------DIBUJO---------------------------------------------------

    pantalla.fill((50, 50, 50))
    pygame.draw.line(pantalla, NEGRO, [0,dim[0]], [dim[1], 0])
    aj = 0
    for i in range(len(cs)):
        if(0<1<3):
            aj = 1
        if(3<i):
            aj = 2
        pygame.draw.rect(pantalla, VIOLETA, [dim[0]-cs[i][0]+1, cs[i][0]+1, cs[i][1]+aj, cs[i][1]+aj], 2)
        
        pygame.draw.rect(pantalla, VERDE, [dim[0]-cs[i][0]-cs[i][1]-1, cs[i][0]-cs[i][1]-1, cs[i][1]+aj, cs[i][1]+aj], 1)
    pygame.display.flip()
    reloj.tick(5)

pygame.quit()
