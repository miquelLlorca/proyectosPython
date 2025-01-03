from multiprocessing.sharedctypes import Value, Array
import os
import signal


dimensiones = [50,50]
res = 1
length = int(dimensiones[0]/res + dimensiones[1]/res)
plano = Array('d', range(length))

for i in range(length):
    plano[i] = 0.0


rx = int(length/4)

if(os.fork()):
    if(os.fork()):
        if(os.fork()): # padre
            for i in range(0, rx):
                plano[i] += 1


        else: # hijo 3
            for i in range(rx*3, rx*4):
                plano[i] += 1
            os.kill(os.getpid(), signal.SIGKILL)


    else: # hijo 2
        for i in range(rx*2, rx*3):
                plano[i] += 1
        os.kill(os.getpid(), signal.SIGKILL)


else: # hijo 1
    for i in range(rx, rx*2):
        plano[i] += 1
    os.kill(os.getpid(), signal.SIGKILL)



os.wait()
os.wait()
os.wait()
for x in plano:
    print(x)

