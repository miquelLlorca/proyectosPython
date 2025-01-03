from engine import Engine
from time import sleep
import os


def read_command_file(path):
    with open(path,'r') as input_file:
        data = input_file.read()
        lines = data.split('\n')
        commands = [x.split(' ') for x in lines] 
        return commands
    
###################################################################################################################
###################################################################################################################
###################################################################################################################

def ramificar():
    # nodo inicial
    
    # while(cola no vacia):
        
    #     if(es hoja): # acaba la partida?
            
    #     else
    #         expandion = ...
    #         meter expansion en cola
    return
###################################################################################################################

def jugar():
    '''
    Standard game flow. Game is played using the specific command format.
    The used commands are printed at the end so the game can be rewatched.
    '''
    engine = Engine()
    commands = []

    while(True):
        engine.show()
        command = input(':\ ').split()
        commands.append(command)
        if(not engine.execute(command)):
            engine.show()
            break
        
    print()
    print('Commands:')
    print(commands)

###################################################################################################################

def auto(path, speed):
    '''
    Plays a predefined sequence of moves that are stored on the path using the specific command format.
    Args:
        - path(str): path to the file.
        - speed(float): determines how fast it will be played, as 1/speed
    '''
    engine = Engine()
    
    commands = read_command_file(path)
    for command in commands:
        engine.show()
        sleep(1/speed)
        if(not engine.execute(command)):
            engine.show()
            break
        
##############################################################################
       
if(__name__ == "__main__"):
    # jugar()

    pwd = '/home/miquel/proyectosPython/JUEGOS/ajedrez/chess_engine/'
    path = os.path.join(pwd, 'commands.txt')
    auto(path, speed=2)

# TODO. tests, estarian bien la verdad