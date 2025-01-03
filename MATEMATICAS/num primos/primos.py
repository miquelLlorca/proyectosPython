''' primos '''

n = int(input('n ='))
cont1 = 0
num = 2

while cont1 < n :
    div = 2
    cont2 = 2
    
    while div <= num :
        
        if num % div == 0 :   
            if num == div :
                cont2 = 1
            else :
                cont2 = 0
                div = num     
        div += 1
        
       
    if cont2 == 1 :
        
            if cont1 == n - 1 :
                cp = '.'
            else :
                cp = ','
                
            print('{}{} '.format(num,cp),end='')
            cont1 += 1 
        
    num += 1
