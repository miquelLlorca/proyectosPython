# porcentajes peso
def calcPeso(pectoral, dorsal, porcentaje):
    lista = []
    p = porcentaje/100
    ejercicios = ['Pectoral','Dorsal','Biceps','Sentadilla','Pectoral abierto'
                  ,'Dorsal mancuerna','Triceps','Hombro']

    for x in ejercicios:
        if x == 'Pectoral':
            peso = pectoral*p
        elif x=='Dorsal':
            peso = dorsal*p
        elif x=='Biceps':
            peso = pectoral*p*0.5
        elif x=='Pectoral abierto':
            peso = pectoral*p*0.5*0.5
        elif x=='Dorsal mancuerna':
            peso = dorsal*p*0.5
        elif x =='Triceps' or x=='Hombro':
            peso = pectoral*p*0.5*0.5
        elif x == 'Sentadilla':
            if porcentaje <= 25:
                peso = 5
            elif porcentaje <= 50:
                peso = 10
            elif porcentaje <= 75:
                peso = 15
            elif porcentaje <= 100:
                peso = 20
        pe = str(int(round(peso,0)))
        lista.append(pe)
    return lista



