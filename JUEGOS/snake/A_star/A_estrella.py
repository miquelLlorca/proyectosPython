import timeit


class Nodo:
    def __init__(self, x, y, g, h, profundidad):
        self.x = x
        self.y = y
        self.padre = None
        self.g = g
        self.h = h
        self.f = g
        self.profundidad = profundidad

    
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    
    
    def __str__(self):
        txt = "("
        txt += str(self.x)
        txt += ", "
        txt += str(self.y)
        txt += ")"
        return txt
        
        
    def ExpandirNodo(self, snake):
        hijos = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                x = self.x+i*snake.tam
                y = self.y+j*snake.tam
                
                if(0<=x<snake.mapa[0]*snake.tam and 0<=y<snake.mapa[1]*snake.tam and abs(i)!=abs(j) and [x, y] not in snake.cola):
                    g = self.g+1 if abs(i)!=abs(j) else self.g+1.5
                    hijos.append(Nodo(x, y, g, self.h, self.profundidad+1))
                    hijos[len(hijos)-1].padre = self
                    
        return hijos

    
    def F(self, meta):
        self.f = self.g + self.h(self, Nodo(meta[0], meta[1], 0, 0, 0))
        


# ===================================================================================================================


def InsertaNodo(lista, nodo):
    if(len(lista)==0):
        lista.append(nodo)
    else:
        for i in range(len(lista)):
            if(lista[i].f >= nodo.f):
                lista.insert(i, nodo)
                break
        if(nodo not in lista):
            lista.append(nodo)
        


# Funciones para H(n)
def AnalisisAnchura(a, b):
    return 0

def DistanciaBloques(a, b):
    return abs(a.x-b.x) + abs(a.y-b.y)

def DistanciaEuclidea(a, b):
    return ( (a.x-b.x)**2 + (a.y-b.y)**2 )**0.5



# Algoritmo
def A_Estrella(serpiente, p0, p1, camino, h, maxProf, debug=False):


    coste = 0
    listaInterior = []
    listaFrontera = [Nodo(p0[0], p0[1], 0, h, 0)]
    
    mejorNodo = None

    while(len(listaFrontera) > 0):
        n = listaFrontera[0] # nodo con menor f(n) #primera version f = g
                             # siempre estara en el 0 
        
        
        if(n.x==p1[0] and n.y==p1[1]): # n es meta
            coste = n.g
            while(n is not None):
                camino.insert(0, [n.x, n.y])
                n = n.padre
                
            return coste
        
        
        else:
            listaFrontera.pop(0)
            listaInterior.append(n)


            if(n.profundidad == maxProf):
                if(mejorNodo is None or mejorNodo.f > n.f):
                    mejorNodo = n
                
            else:
                for m in n.ExpandirNodo(serpiente): # por cada hijo de n
                    if(m not in listaInterior):
                        
                        found = False
                        for i in range(len(listaFrontera)):                            # se busca el nodo en listaFrontera
                            if(m.x == listaFrontera[i].x and m.y == listaFrontera[i].y):
                                found = True
                                if(m.g < listaFrontera[i].g):                          # si se encuentra y la nueva g es mejor...
                                    listaFrontera[i].padre = n
                                    listaFrontera[i].g = m.g
                                    listaFrontera[i].F(p1)
                                break
                        
                        
                        if(not found):
                            m.F(p1)
                            InsertaNodo(listaFrontera, m) # se inserta el nuevo nodo en la posicion adecuada

    n = mejorNodo
    while(n is not None):
        camino.insert(0, [n.x, n.y])
        n = n.padre

    if(len(camino) < 2):
        camino = [Nodo(p0[0], p0[1], 0, h, 0)]
        n = Nodo(p0[0], p0[1], 0, h, 0)
        for m in n.ExpandirNodo(serpiente):
            if(m.f < camino[0].f):
                camino[0] = m
        
        camino[0] = [camino[0].x, camino[0].y]
    else:
        camino.pop(0)
    
    return -1
    
    
    
    
    
'''
lg A*
    listaInterior = vacio
    listaFrontera = inicio
    
    mientras listaFrontera no esté vacía
        n = obtener nodo de listaFrontera con menor f(n) = g(n) + h(n)
        
        si n es meta devolver
            reconstruir camino desde la meta al inicio siguiendo los punteros
            Salir
        sino
            listaFrontera.del(n)
            listaInterior.add(n)
            
            para cada hijo m de n que no esté en lista interior
                g’(m) = n·g + c(n, m) //g del nodo a explorar m
                si m no está en listaFrontera
                    almacenar la f, g y h del nodo en (m.f, m.g, m.h) 
                    m.padre = n
                    listaFrontera.add(m)
                sino si g’(m) es mejor que m.g //Verificamos si el nuevo camino es mejor
                    m.padre = n
                    recalcular f y g del nodo m
                fsi
            fpara
        fsi
    fmientras
    
    Error, no se encuentra solución
Falg
'''

    