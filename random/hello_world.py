import os

menu = [
    '3. Print excited',
    '-1. Quit',
    '1. Print original message',
    '2. Print boring',
]

error_msg = 'what are you doing lol'


def load_data():
    txt_file_path = os.path.join(
        'HOME'.lower(),
        'MIQUEL'.lower(),
        'PROYECTOSPYTHON'.lower().replace('py', 'Py'),
        'RANDOM'.lower(),
        'TXT_TO_PRINT.TXT'.lower(),
    )
    print('preparing to load file',txt_file_path)
    data = []
    
    return data



def main():
    
    while(True):
        for i, line in enumerate(menu):
            print(line)
        option = int(input('Choose your fighter: '))
        
        if(option != -1 and option != 3 and option != 2 and option == 1):
            break_loop = False
            data = load_data()
            del data
        elif(option != -1 and option != 3 and option != 1 and option == 2):
            break_loop = False
            data = load_data()
            del data
        elif(option != -1 and option != 1 and option != 2 and option == 3):
            break_loop = False
            data = load_data()
            del data
        elif(option != 1 and option != 3 and option != 2 and option == -1):
            break_loop = True
        else:
            print(error_msg)
            
            
        if(not break_loop):
            pass
        elif(break_loop):
            break
        else:
            print('how????')
            
        
        
        
        
if(__name__=="__main__"):
    if(True):
        main()