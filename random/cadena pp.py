

def sust(c):
    nc = ''
    for x in c:
        if x == 'p':
            nc += 'pepe'
        else:
            nc += 'E'
    return nc


cad = 'pepe'
print(cad)
print(sust(cad))
for i in range(5):
    cad = sust(cad)
    print(sust(cad))
    
