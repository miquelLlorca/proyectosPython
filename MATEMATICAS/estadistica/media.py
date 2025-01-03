def media(x):
    suma = 0
    long = len(x)
    for i in range(0,len(x)):
        term = x[i]
        suma += term
    return round(suma/long,5)
    
def desv(x):
    n = len(x)
    m = media(x)
    suma = 0
    for i in range(0,len(x)):
        suma += (x[i] - m)**2
    return round((suma / (n - 1))**0.5, 5)

def contar(x, y):
    suma = 0
    for i in range(0, len(y)):
        if y[i] == x:
            suma += 1
    return suma
        
def moda(x):
    num = None
    veces1 = 0
    for i in range(0,len(x)): 
        veces = contar(x[i], x)
        if veces > veces1:
            veces1 = veces
            num = x[i]
      
    return num

'''
a = input().split()
A = [float(x) for x in a]
print(media(A))
print(desv(A))
#print(moda(A))
'''
