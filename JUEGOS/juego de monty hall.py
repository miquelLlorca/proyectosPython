#juego de monty hall
from random import choice
n = 10
win = 0
cambio = 0

for i in range(n):
    a = choice(('coche','cabra','cabra'))

    if a == 'coche':
        b = 'cabra'
        c = 'cabra'

    else:
            b = choice(('coche','cabra'))
            if b == 'coche':
                c = 'cabra'
            else:
                c = 'coche'
                
    eleccion = input('Elige una puerta [a,b,c]: ')

    if eleccion == 'a':
        if a == 'coche':
            x = choice(('b','c'))
            print('La puerta {} tiene una cabra.'.format(x))
        elif b == 'coche':
            x = 'c'
            print('La puerta {} tiene una cabra.'.format(x))
        elif c == 'coche':
            x = 'b'
            print('La puerta {} tiene una cabra.'.format(x))
    elif eleccion == 'b':
        if a == 'coche':
            x = 'c'
            print('La puerta {} tiene una cabra.'.format(x))
        elif b == 'coche':
            x = choice(('a','c'))
            print('La puerta {} tiene una cabra.'.format(x))
        elif c == 'coche':
            x = 'a'
            print('La puerta {} tiene una cabra.'.format(x))
    elif eleccion == 'c':
        if a == 'coche':
            x = 'b'
            print('La puerta {} tiene una cabra.'.format(x))
        elif b == 'coche':
            x = 'a'
            print('La puerta {} tiene una cabra.'.format(x))
        elif c == 'coche':
            x = choice(('a','b'))
            print('La puerta {} tiene una cabra.'.format(x))

    sn = input('¿Quieres cambiar tu elección?[s/n]')
    if sn == 's':
        e = ['a','b','c']
        for j in range(3):
            if e[j]!= eleccion and e[j] != x:
                eleccion2 = e[j]
                break
        
        if eleccion2 == 'a':
            if a == 'coche':
                print('¡Has ganado!')
                win += 1
            else:
                print('Has perdido.')
        elif eleccion2 == 'b':
            if b == 'coche':
                print('¡Has ganado!')
                win += 1
            else:
                print('Has perdido.')
        elif eleccion2 == 'c':
            if c == 'coche':
                print('¡Has ganado!')
                win += 1
            else:
                print('Has perdido.')
        cambio += 1
    elif sn == 'n':
        if eleccion == 'a':
            if a == 'coche':
                print('¡Has ganado!')
                win += 1
            else:
                print('Has perdido.')
        elif eleccion == 'b':
            if b == 'coche':
                print('¡Has ganado!')
                win += 1
            else:
                print('Has perdido.')
        elif eleccion == 'c':
            if c == 'coche':
                print('¡Has ganado!')
                win += 1
            else:
                print('Has perdido.')
    print('-'*60)

print()
print('Has hecho {} partidas, {} ganadas, {} cambios'.format(n, win, cambio))
