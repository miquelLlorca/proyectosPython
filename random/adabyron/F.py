nC = int(input())

for i in range(nC):
    linea = input()
    x = int(linea[0])

    nms = [1, 3]
    j = 1
    while(nms[j] + nms[j-1] != x):
        nms.append(nms[j] + 2)
        j += 1
        
    linea = linea[3, len(linea)-1]
    print(linea)
    
    for c in linea:
        if()
        nL.append(c)
