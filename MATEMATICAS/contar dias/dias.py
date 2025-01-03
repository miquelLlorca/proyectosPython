''' 31 : enero, marzo, mayo, julio, sept, nov -- 1, 3, 5, 7, 9, 11
30 : mayo, julio, oct, dic -- 4, 6, 8, 10, 12
28/29 : febrero -- 2
'''
#21-06-2000, 20-05-2019, 6907
def fecha(f):
    d = ''
    m = ''
    a = ''
    for i in range(len(f)):
        if i < 2:
            d += f[i]
        if i > 2 and i < 5:
            m += f[i]
        if i > 5:
            a += f[i]
    return int(d), int(m), int(a)

def comprobar(f):
    if f[1] <= 12 and f[0] <= 31:
        if fecha1[0] == 31:
            if fecha1[1] not in m30 and fecha1[1] != 2:
                return True
            else: return False
        return True
    else:
        return False

def ordenar(f1, f2): #devuelve menor-mayor
    if f1[2] > f2[2]:
        return f2, f1
    if f1[2] < f2[2]:
        return f1, f2

    if f1[1] > f2[1]:
        return f2, f1
    if f1[1] < f2[1]:
        return f1, f2

    if f1[0] > f2[0]:
        return f2, f1
    if f1[0] < f2[0]:
        return f1, f2

m31 = [1, 3, 5, 7, 9, 11]
m30 = [4, 6, 8, 10, 12]
diastotales = 0

print('Introduce dos fechas (dd-mm-aaaa)')
f1 = input('Fecha 1: ')
f2 = input('Fecha 2: ')

fecha1 = fecha(f1)
fecha2 = fecha(f2)

c1 = comprobar(fecha1)
c2 = comprobar(fecha2)
if c1 and c2:
    correcto = True

if correcto:
    f1, f2 = ordenar(fecha1, fecha2)
    años = f2[2] - f1[2]
    if años > 1:
        diastotales += 365*(años-1)
    for i in range(f1[2]+1, f2[2]):
        if i%4 == 0:
            diastotales += 1

    for i in range(f1[1]+1, 13):
        if i in m30:
            diastotales += 30
        if i in m31:
            diastotales += 31
        if i == 2:
            if f1[2]%4 == 0:
                diastotales += 29
            else:
                diastotales += 28
    for i in range(1, f2[1]):
        if i in m30:
            diastotales += 30
        if i in m31:
            diastotales += 31
        if i == 2:
            if f1[2]%4 == 0:
                diastotales += 29
            else:
                diastotales += 28
                
    if f1[1] in m30:
        dias = 30
    if f1[1] in m31:
        dias = 31
    if f1[1] == 2:
        if f1[2]%4 == 0:
            dias = 29
        else:
            dias = 28   
    
    diastotales += dias -f1[0]
    diastotales += f2[0]
    
print('Dias: ',diastotales)
print('Semanas: ',round(diastotales/7, 2))
print('Meses: ',round(diastotales/30, 2))
print('Años: ',round(diastotales/365, 2))
