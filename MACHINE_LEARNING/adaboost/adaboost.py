import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from random import randrange


def adaptar_conjuntos(mnist_X, mnist_Y):
    print("Adaptando conjuntos...")

    n = len(mnist_X)
    size = len(mnist_X[0])
    X = mnist_X.reshape((n, size*size)) # se usa reshape para adaptar X
    Y = np.full((10, n), -1, dtype = int) # se incializa Y con -1
    
    for i in range(n):
        Y[mnist_Y[i]][i] = 1            # solo se cambian los 1
        
    return X, Y


# Esta funcion genera un clasificador para la dimension especificada
def generar_clasificador_debil(dimension_datos):
    pixel = randrange(0, dimension_datos) # pixel en el que aplicar el cd
    umbral = randrange(0, 256)            # valor a comparar con el pixel 
    direccion = randrange(-1, 2, 2)       # direccion en la que mirar

    return (pixel, umbral, direccion)


# Esta funcion aplica el clasificador debil a una imagen concreta
def aplicar_clasificador_debil(clasificador, imagen):
    if(clasificador[2]==1):
        if(imagen[clasificador[0]] > clasificador[1]):
            return 1
        return -1
    if(imagen[clasificador[0]] <= clasificador[1]):
        return 1
    return -1


# Esta funcion aplica el clasificador debil a todas las imagenes y compara su resultado a las etiquetas
def obtener_error(clasificador, X, Y, D):
    errorTotal = 0
    
    for i in range(len(X)):
        if(aplicar_clasificador_debil(clasificador, X[i]) != Y[i]):
            errorTotal += D[i] # si el clasificador falla, suma el peso de la imagen
        
    return errorTotal



def adaboost(X, Y, T, A):

    print("Inicio entrenamiento.")
    clasificadores_debiles = [[] for i in range(10)]
    alphas = [[] for i in range(10)]


    for n in range(10): # para cada digito...
        print("- Creando clasificador para", n)
        D = []
        Zt = 1
        for i in range(len(X)): # se inicializa el vector de pesos
            D.append(1/len(X))
        
        for i in range(T): # T clasificadores debiles
            CD = []
            errorMin = 100000000000000

            for j in range(A): # A pruebas aleatorias
                cd = generar_clasificador_debil(len(X[0]))
                err = obtener_error(cd, X, Y[n], D)
                if(err < errorMin):
                    errorMin = err
                    CD = cd

            alpha = 0.5 * np.log2((1-errorMin+0.01)/(errorMin+0.01)) # se calcula el peso para el clasificador debil

            clasificadores_debiles[n].append(CD)
            alphas[n].append(alpha)
            
            for i in range(len(X)): # se calculan los nuevos pesos para las imagenes
                D[i] = D[i]*np.exp(-alpha*Y[n][i]*aplicar_clasificador_debil(CD,X[i]))
            Zt = sum(D)
            for i in range(len(X)): # se normaliza el vector
                D[i] = D[i]/Zt
            
    return (clasificadores_debiles, alphas)


def clasificar_imagenes(CF, alphas, X, Y):
    results = [0 for i in range(10)]
    aciertos = [0 for i in range(10)]

    print("Evaluando imagenes...")
    step = int(len(X)/100)

    for i in range(len(X)): # Para cada imagen
        results = [0 for i in range(10)]

        for n in range(10): # Para cada clasificador fuerte
            for j in range(len(CF[n])): # Para cada cd en cf
                if(aplicar_clasificador_debil(CF[n][j], X[i]) == 1):
                    results[n] += alphas[n][j]
                else:
                    results[n] -= alphas[n][j]

            if(results[n] >= 0 and Y[n][i] == 1):
                aciertos[n] += 1
            elif(results[n] < 0 and Y[n][i] == -1):
                aciertos[n] += 1

    media = 0
    for i in range(10):
        aciertos[i] /= len(X)
        aciertos[i] *= 100
        media += aciertos[i]
        aciertos[i] = str(round(aciertos[i], 4)) + "%"
    return aciertos, media/10


def clasificar_imagen(CF, alphas, imagen):

    results = [0 for i in range(10)]

    for n in range(10): # Para cada clasificador fuerte
        for j in range(len(CF[n])): # Para cada cd en cf
            if(aplicar_clasificador_debil(CF[n][j], imagen) == 1):
                results[n] += alphas[n][j]
            else:
                results[n] -= alphas[n][j]

    max = -100000000000
    pos = 0
    maxAbs = -100000000000
    for i in range(10):
        if(results[i] >= max):
            max = results[i]
            pos = i
        if(abs(results[i]) >= maxAbs):
            maxAbs = results[i]
    
    return pos, maxAbs, results






# ============================================================ MAIN ===============================


if(__name__ == "__main__"):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    print()
    print()

    XTr, YTr = adaptar_conjuntos(x_train, y_train)
    XTe, YTe = adaptar_conjuntos(x_test, y_test)
    print()

    T = 10  # numero de cd en cf
    A = 10  # numero de pruebas aleatorias

    CF, alphas = adaboost(XTr, YTr, T, A)

    results, media = clasificar_imagenes(CF, alphas, XTe, YTe)
    for i in range(10):
        print(f"CF {i}: {results[i]}")

    print(f"Media: {media}%")


    filename = input("Nombre de archivo:")
    file = open(filename, "w")
    file.write(str(T)+"\n")
    for i in range(10):
        for j in range(T):
            txt = ""
            txt += str(CF[i][j][0])
            txt += " "
            txt += str(CF[i][j][1])
            txt += " "
            txt += str(CF[i][j][2])
            txt += "\n"
            file.write(txt)
            file.write(str(alphas[i][j])+"\n")


    file.close()
