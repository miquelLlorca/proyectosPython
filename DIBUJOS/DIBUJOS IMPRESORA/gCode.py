def creaGcode(ls, cs):
    '''
    G1 X10 F3600  -  G1 movimiento, XYZ N mm, F velocidad
    Z = altura
    '''
    esc = 5
    offset = 75

    nombre = input("Introduce el disco: ")
    nombre += ":\\"
    nombre += input("Introduce el nombre: ")
    nombre += ".gcode"
    f = open(nombre, 'w')

    f.write("G21\n")
    f.write("G28\n")
    f.write("G1 Z35 F1000\n")

    for i in range(len(ls)): # lineas
        f.write("G1 ")
        if(ls[i].x[0] != 0):
            f.write("X{} ".format(offset + int(ls[i].x[0]/esc)))
        if(ls[i].x[1] != 0):
            f.write("Y{} ".format(offset + int(ls[i].x[1]/esc)))
        f.write("F3600 \n")

        f.write("G1 Z25 F1000\n")

        f.write("G1 ")
        if(ls[i].y[0] != 0):
            f.write("X{} ".format(offset + int(ls[i].y[0]/esc)))
        if(ls[i].y[1] != 0):
            f.write("Y{} ".format(offset + int(ls[i].y[1]/esc)))
        f.write("F3600 \n")

        if(i<len(ls)-1 and not(ls[i+1].x[0] == ls[i].y[0] and ls[i+1].x[1] == ls[i].y[1])):
            f.write("G1 Z35 F1000\n")
            
    f.write("G28\n")
    f.close()
