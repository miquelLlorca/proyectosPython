from time import sleep

CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 
         't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', 
         '4', '5', '6', '7', '8', '9', '0', ',', '.', '-',
         ' ', '(', ')', ';', ':', '<', '>', '=', '_', '/',
         'á', 'é', 'í', 'ó', 'ú', '?', '¿', '¡', '!', '+',
         '*', '#', 
         ]


def GetEquivalent(c, d):
    return CHARS[(CHARS.index(c)+d)%len(CHARS)]

def GetData(fileName):
    try:
        file = open(fileName, 'r')
        error = False
    except:
        print("404: File not found.")
        return []

    data = []
    line = file.readline()
    while(line != ""):
        data.append(line)
        line = file.readline()
    file.close()

    return data


def WriteData(data, fileName):
    with open(fileName+'.out', 'w') as file:
        for line in data:
            file.write(line)

    return

def EnCrypt(data, password):
    d = sum([ord(c) for c in password]) # desfase
    newData = []

    while(data != []):
        line = data.pop(0)# coge primera linea y quita el \n
        line = line.lower()
        if(line[-1:] == "\n"):
            line = line[:-1]

        newLine = ''

        for c in line:
            newLine += GetEquivalent(c, d)

        newData.append(newLine)
    return newData


def DeCrypt(data, password):
    d = sum([ord(c) for c in password]) # desfase
    newData = []

    while(data != []):
        line = data.pop(0) # coge primera linea y quita el \n
        line = line.lower()
        if(line[-1:] == "\n"):
            line = line[:-1]

        newLine = ''
        for c in line:
            newLine += GetEquivalent(c, -d)

        newData.append(newLine)
    return newData





if(__name__ == "__main__"):



    print(" - FILE ENCRYPTOR/DECRYPTOR - ")
    # fileName = 'test.txt'
    # pswd = 'mirea2342022'
    
    
    fileName = input('File: ')
    pswd = input('Password: ')
    mode = input('Encrypt/Decrypt (e/d): ')
    
    if(mode.lower() == 'e'):
        WriteData(EnCrypt(GetData(fileName), pswd), fileName)
    elif(mode.lower() == 'd'):
        WriteData(DeCrypt(GetData(fileName), pswd), fileName)
    else:
        print('Error: wrong mode selected.')

    sleep(1)

    
    '''    txt = ['á é í ó ú']
    print(DeCrypt(EnCrypt(txt, 'a'),'a'))    

'''