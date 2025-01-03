from tablero import Tablero
from colorama import Fore
import os

class Engine:
    def __init__(self, display_mode='terminal'):
        self.display_mode = display_mode
        self.tablero = Tablero()
        
    def execute(self, command):
        pos = command[1:]
        os.system('clear')
        print(f':\\ {" ".join(command)}')
        error = False
        try:
            if(command[0] == 's'):
                self.tablero.get_available_moves(pos)
            elif(command[0] == 'm'):
                self.tablero.move(pos)
            elif(command[0] == 'q'):
                return False
            else:
                error = True
        except:
            error = True
        if(error):
            print(f'{Fore.RED}Error{Fore.RESET}: command format [s,m] [a-b] [1-8]')
        return True
    
    def show(self, pantalla=None):
        if(self.display_mode == 'terminal'):
            print(self.tablero)


