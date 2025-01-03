import pygame
import random
from clases import Level, NuevoTablero, findNextLevel, select
from os import system

    
NEGRO = (0, 0 ,0)



# =========================================================== MAIN ===========================================================
system("clear")

print("Elige una opcion:")
print("1. Jugar")
print("2. Crear niveles")
print("3. Salir")
op = int(input())

while(op != 3):

    if(op == 2):
        tabl = NuevoTablero(findNextLevel()[1], n=10, size=76)

    elif(op == 1):
        try:
            tabl = Level(findNextLevel()[0]) # de aqui se cargara un nivel
        except:
            print("No hay ningun nivel creado.")
            op = 2
            tabl = NuevoTablero(findNextLevel()[1], n=10, size=50)

    if(op == 2):
        print("Click para añadir/quitar bloques")
        print("C para cañon")
        print("G para globo")
        print("P para portal")

    selectEnt = [0, 0, 0] # cañon, globo, portal
    save = False
    size = tabl.size
    n = tabl.n

    transicion = False # transicion entre dos niveles de IGUAL tamaño
    newWindow = False # transicion entre dos niveles de DISTINTO tamaño


    pygame.init()
    dimensiones = [n*size, n*size]
    pantalla = pygame.display.set_mode(dimensiones) 
    pygame.display.set_caption("Fill")
    hecho = False
    reloj = pygame.time.Clock()

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                hecho = True
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(op == 2 and selectEnt[2]!=1):
                    pos = [int((x/size)%n) for x in pygame.mouse.get_pos()]
                    tabl.Set(pos, select(selectEnt))

            if evento.type == pygame.MOUSEBUTTONUP:
                if(op == 2 and selectEnt[2]):
                    p2 = [int((x/size)%n) for x in pygame.mouse.get_pos()]
                    tabl.Set(pos, "P", pos2=p2)

            if evento.type == pygame.KEYDOWN:
                if(not transicion): # durante una transicion no se puede hacer nada
                    if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                        tabl.Slide(1, -1)
                    elif evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                        tabl.Slide(1, 1)
                    elif evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                        tabl.Slide(0, 1)
                    elif evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
                        tabl.Slide(0, -1)

                    elif evento.key == pygame.K_r: # reset
                        tabl.Reset()

                    if(op == 2):
                        if evento.key == pygame.K_KP_ENTER: # keypad enter para guardar
                            hecho = True
                            save = True
                        elif evento.key == pygame.K_c: # cañones
                            selectEnt = [1, 0, 0]
                        elif evento.key == pygame.K_g: # globo
                            selectEnt = [0, 1, 0]
                        elif evento.key == pygame.K_p: # portal
                            selectEnt = [0, 0, 1]
                        elif evento.key == pygame.K_b: # bloque
                            selectEnt = [0, 0, 0]
                        elif evento.key == pygame.K_z: # deshace el ultimo entity
                            tabl.entities = tabl.entities[:-1]
                            a=0

        # ---------------------------------------------------LÓGICA---------------------------------------------------
        tabl.Update()
        
        if(not transicion and op == 1 and tabl.Finished()):
            transicion = True
            tabl2 = Level(findNextLevel()[0])
            iters = [0, 0]

            if(tabl.n*tabl.size != tabl2.n*tabl2.size):
                newWindow = True
        
        if(transicion and iters[0] == n):
            tabl = tabl2
            transicion = False

        if(newWindow):
            break

        # ---------------------------------------------------DIBUJO---------------------------------------------------

        


        pantalla.fill((50, 50, 50))
        
        if(not transicion):
            for i in range(n):
                for j in range(n):
                    if(tabl.tablero[i][j] == "B"):
                        pygame.draw.rect(pantalla, NEGRO, [size*i, size*j, size, size])

                        if(i>0 and tabl.tablero[i-1][j] != "B"):
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, size*j, int(size/8), size])
                            pygame.draw.rect(pantalla, tabl.colorBloque, [int(size*(i+0.25)), size*j, 2, size])

                        if(j>0 and tabl.tablero[i][j-1] != "B"):
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, size*j, size, int(size/8)])
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, int(size*(j+0.25)), size, 2])

                        if(i<n-1 and tabl.tablero[i+1][j] != "B"):
                            pygame.draw.rect(pantalla, tabl.colorBloque, [int(size*(i+7/8))+1, size*j, int(size/8), size])
                            pygame.draw.rect(pantalla, tabl.colorBloque, [int(size*(i+0.75)), size*j, 2, size])

                        if(j<n-1 and tabl.tablero[i][j+1] != "B"):
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, int(size*(j+7/8))+1, size, int(size/8)])
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, int(size*(j+0.75)), size, 2])

                        # faltaria hacer las esquinas pero probablemente mucho texto xd

                    elif(tabl.tablero[i][j] == "F"):
                        pygame.draw.rect(pantalla, tabl.colorFill, [size*i, size*j, size, size])

            for e in tabl.entities:
                if(e.tipo == "C"):
                    pygame.draw.rect   (pantalla, NEGRO, [size*e.pos[0], size*e.pos[1], size, size])
                    pygame.draw.rect   (pantalla, tabl.colorBloque, [size*e.pos[0]+1, size*e.pos[1]+1, size-3, size-3], 4)
                    pygame.draw.ellipse(pantalla, tabl.colorBloque, [size*e.pos[0]+4, size*e.pos[1]+4, size-8, size-8], 5)
                #if(e.tipo == "G"):
                    
            pygame.draw.ellipse(pantalla, (255, 255, 0), [size*tabl.player.pos[0]+2, size*tabl.player.pos[1]+2, size-4, size-4])
            pygame.draw.ellipse(pantalla, NEGRO, [size*tabl.player.pos[0]+2, size*tabl.player.pos[1]+2, size-4, size-4], 4)



        else:
            for i in range(iters[0]):
                for j in range(iters[0]):
                    if(tabl2.tablero[i][j] == "B"):
                        pygame.draw.rect(pantalla, NEGRO, [size*i, size*j, size, size])

                        if(i>0 and tabl2.tablero[i-1][j] != "B"):
                            pygame.draw.rect(pantalla, tabl2.colorBloque, [size*i, size*j, int(size/8), size])
                            pygame.draw.rect(pantalla, tabl2.colorBloque, [int(size*(i+0.25)), size*j, 2, size])

                        if(j>0 and tabl2.tablero[i][j-1] != "B"):
                            pygame.draw.rect(pantalla, tabl2.colorBloque, [size*i, size*j, size, int(size/8)])
                            pygame.draw.rect(pantalla, tabl2.colorBloque, [size*i, int(size*(j+0.25)), size, 2])

                        if(i<n-1 and tabl2.tablero[i+1][j] != "B"):
                            pygame.draw.rect(pantalla, tabl2.colorBloque, [int(size*(i+7/8))+1, size*j, int(size/8), size])
                            pygame.draw.rect(pantalla, tabl2.colorBloque, [int(size*(i+0.75)), size*j, 2, size])

                        if(j<n-1 and tabl2.tablero[i][j+1] != "B"):
                            pygame.draw.rect(pantalla, tabl2.colorBloque, [size*i, int(size*(j+7/8))+1, size, int(size/8)])
                            pygame.draw.rect(pantalla, tabl2.colorBloque, [size*i, int(size*(j+0.75)), size, 2])
                        

            for i in range(iters[0], n):
                for j in range(iters[0], n):
                    if(tabl.tablero[i][j] == "B"):
                        pygame.draw.rect(pantalla, NEGRO, [size*i, size*j, size, size])

                        if(i>0 and tabl.tablero[i-1][j] != "B"):
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, size*j, int(size/8), size])
                            pygame.draw.rect(pantalla, tabl.colorBloque, [int(size*(i+0.25)), size*j, 2, size])

                        if(j>0 and tabl.tablero[i][j-1] != "B"):
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, size*j, size, int(size/8)])
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, int(size*(j+0.25)), size, 2])

                        if(i<n-1 and tabl.tablero[i+1][j] != "B"):
                            pygame.draw.rect(pantalla, tabl.colorBloque, [int(size*(i+7/8))+1, size*j, int(size/8), size])
                            pygame.draw.rect(pantalla, tabl.colorBloque, [int(size*(i+0.75)), size*j, 2, size])

                        if(j<n-1 and tabl.tablero[i][j+1] != "B"):
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, int(size*(j+7/8))+1, size, int(size/8)])
                            pygame.draw.rect(pantalla, tabl.colorBloque, [size*i, int(size*(j+0.75)), size, 2])

                    elif(tabl.tablero[i][j] == "F"):
                        pygame.draw.rect(pantalla, tabl.colorFill, [size*i, size*j, size, size])


            iters[1] += 1
            if(iters[1]==5):
                iters = [iters[0]+1, 0]


        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


    if(save == True):
        tabl.Save()

    
    if(not newWindow):
        system("clear")
        print("Elige una opcion:")
        print("1. Jugar")
        print("2. Crear niveles")
        print("3. Salir")
        op = int(input())
    else:
        op = 1
