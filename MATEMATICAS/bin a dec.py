#binario a decimal
def bad():
    b = input('Binario: ')
    B = []
    for i in b:
        if i == '0' or i =='1':
            B.append(i)

    suma = 0
    for i in range(len(B)-1,-1,-1):
        fact = int(B[4-i])
        term = fact*2**i
        suma += term
    print('Decimal:',suma)
    print()
    
#decimal a binario
def dab():
    d = int(input('Decimal: '))
    B2 = []
    c = 0
    print('Binario: ',end='')
    while d >= 1:
        if c == 0:
            B2.append(d%2)
            e = d
            d = e//2
            c += 1
        elif c == 1:
            B2.append(d%2)
            e = d
            d = e//2

    for i in range(len(B2)-1, -1, -1):
        print(B2[i],end='')

    print()
    print()
        
salir = 'n'

while salir != 'si':
    dec = input('Binario -> Decimal (1), Decimal -> Binario (2): ')
    if dec == '1':
        bad()
    elif dec == '2':
        dab()
    salir = input('Salir? (si/no)')
    
