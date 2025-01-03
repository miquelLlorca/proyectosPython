import pygame
import random
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
 
class Bloque(pygame.sprite.Sprite):
     
    def __init__(self, color, largo, alto):         
        # Llama al constructor de la clase padre (Sprite) 
        super().__init__() 

        self.image = pygame.Surface([largo, alto])
        self.image.fill(BLANCO)
        self.image.set_colorkey(BLANCO)
 
        # Obtenemos el objeto rectángulo que posee las dimensiones de la imagen
        # Actualizamos la posición de ese objeto estableciendo los valores para 
        # rect.x y rect.y
        self.rect = self.image.get_rect()
        
        # Dibuja la elipse
        pygame.draw.ellipse(self.image, color, [0, 0, largo, alto])
        pygame.draw.ellipse(self.image, NEGRO, [0, 0, largo, alto], 1)

pygame.init()
dimensiones = [1000, 750]
pantalla=pygame.display.set_mode(dimensiones)
marcador = 0

# Esta es una lista de 'sprites.' Cada bloque en el programa es
# añadido a la lista. La lista es gestionada por una clase llamada 'Group.'
bloque_lista = pygame.sprite.Group()
 
# Esta es una lista de cada uno de los sprites. Así como del resto de bloques y el bloque protagonista..
listade_todoslos_sprites = pygame.sprite.Group()
 
for i in range(10000):
    # Esto representa un bloque
    bloque = Bloque((255, 255, 0), 15, 15)
    # Establecemos una ubicación aleatoria para el bloque
    bloque.rect.x = random.randrange(dimensiones[0])
    bloque.rect.y = random.randrange(dimensiones[1])
    # Añadimos el  bloque a la lista de objetos
    bloque_lista.add(bloque)
    listade_todoslos_sprites.add(bloque)
 
# Creamos un bloque protagonista ROJO
protagonista = Bloque(ROJO, 30, 30)
listade_todoslos_sprites.add(protagonista)

hecho = False
reloj = pygame.time.Clock()

# -------- Bucle principal del Programa -----------
while not hecho:
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pulsó salir
            hecho = True # Marcamos que hemos terminado y salimos del bucle
 

    pantalla.fill(BLANCO)
    pos = pygame.mouse.get_pos()
    protagonista.rect.x = pos[0]-15
    protagonista.rect.y = pos[1]-15
     
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, True)  # True borra los que coinciden
    
    for bloque in lista_impactos_bloques:
        marcador += 1
        print(marcador)
         
    listade_todoslos_sprites.draw(pantalla)
     
    reloj.tick(60)
    pygame.display.flip()
 
pygame.quit()
