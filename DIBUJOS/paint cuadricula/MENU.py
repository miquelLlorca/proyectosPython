from cuadr import cuadricula
from triang import triangulica
from noPlantilla import sinPlantilla

op = 0

while(op != 4):
    print(" ---  Generador dibujo --> Gcode  --- ")
    print("      1. Plantilla cuadrada.")
    print("      2. Plantilla isometrica.")
    print("      3. Sin plantilla.")
    print("      4. Salir.")
    print()
    op = int(input("Opcion: "))

    if(op==1):
        cuadricula()
    elif(op==2):
        triangulica()
    elif(op==3):
        sinPlantilla()
    elif(op==4):
        print("Bye.")
    else:
        print("Opcion incorrecta.")
    print()


