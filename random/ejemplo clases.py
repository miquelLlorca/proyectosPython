class Persona:
    def __init__(self, nombre, dni, edad): #definir la forma
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.patata = edad+23
        
    def __str__(self): #print
        cadena = ''
        cadena += 'Nombre: {}\n'.format(self.nombre)
        cadena += 'DNI: {}\n'.format(self.dni)
        cadena += 'Edad: {}'.format(self.edad)
        return cadena
    
    def iniciales(self): 
        cadena = ''
        for x in self.nombre:
            if x >= 'A' and x <='Z':
                cadena += x
                cadena +='. '
        return cadena

    def copia(self): #se define para poder crear copias en las que realizar cambios sin que afecten al anterior
        nuevo = Persona(self.nombre, self.dni, self.edad)
        return nuevo
    
    
toni = Persona('Ant Per','123x',16)
print(toni.nombre)
print(toni.dni)
print(toni.patata)
print(toni.iniciales())

print()
print(toni)
