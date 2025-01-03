import numpy as np


def get_cadena(cadena):
    new_cadena = ''
    
    for i in range(10):
        new_cadena += '\n'
        
    for i in range(0,len(cadena),1):
        prints = []
        while(len(prints) != i):
            if((new_num := np.random.randint(len(cadena))) not in prints):
                prints.append(new_num)
            
        
        for j, c in enumerate(cadena):
            if(j in prints):
                new_cadena += c
            else:
                new_cadena += ' '
                
        new_cadena += '\n'
        
    for i in range(5):
        new_cadena += cadena
        new_cadena += '\n'
        
    return new_cadena
    
    
if(__name__ == "__main__"):
    cadena = 'You may live to see man-made horrors beyond your comprehension...'
    new_cadena = get_cadena(cadena)
    
    print(new_cadena)
    with open('arte.txt','w') as out_file:
        out_file.write(new_cadena)