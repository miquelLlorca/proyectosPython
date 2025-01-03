from editor import *
from os import system


name = "scolano.png" #input("Name: ")
system("cd ~/Escritorio/proyectosPython/ANIMACIONES/modImagenes")
imagen = Image.open(name)
dimensiones = imagen.size
foto = Pixeles(imagen)
foto.Aristas(125)
txt = foto.ToAscii(2, type="discreto") # podria probar de aplicar el filtro de aristas
                        # y paralelizarlo tambien estaria guapo oye
#print(txt)

name = "scoascii.txt"#input("File name: ")
file = open(name, "w")
file.write(txt)
file.close()