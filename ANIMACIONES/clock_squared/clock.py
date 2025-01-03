import pygame
import numpy as np





###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################

# Clock STATES for big clock
FULL_H     = [180,0]
HALF_RIGHT = [0,0]
HALF_LEFT  = [180,180]

FULL_V    = [90,270]
HALF_UP   = [270,270]
HALF_DOWN = [90,90]

CORNER_UP_RIGHT = [180,90]
CORNER_UP_LEFT  = [0,90]
CORNER_DOWN_RIGHT = [180,270]
CORNER_DOWN_LEFT  = [270,0]

VOID = [135, 315]


# NUMBERS
NUM_0 = [
    [CORNER_UP_LEFT, CORNER_UP_RIGHT],
    [FULL_V, FULL_V],
    [CORNER_DOWN_LEFT, CORNER_DOWN_RIGHT],
]

NUM_1 = [
    [VOID, CORNER_UP_RIGHT],
    [VOID, FULL_V],
    [VOID, HALF_UP],
]

NUM_2 = [
    [HALF_RIGHT, CORNER_UP_RIGHT],
    [CORNER_UP_LEFT, CORNER_DOWN_RIGHT],
    [CORNER_DOWN_LEFT, HALF_LEFT],
]

NUM_3 = [
    [FULL_H, CORNER_UP_RIGHT],
    [HALF_RIGHT, CORNER_DOWN_RIGHT],
    [FULL_H, CORNER_DOWN_RIGHT],
]

NUM_4 = [
    [FULL_V, HALF_DOWN],
    [CORNER_DOWN_LEFT, CORNER_DOWN_RIGHT],
    [VOID, FULL_V],
]

NUM_5 = [
    [CORNER_UP_LEFT, HALF_LEFT],
    [CORNER_DOWN_LEFT, CORNER_UP_RIGHT],
    [HALF_RIGHT, CORNER_DOWN_RIGHT],
]

NUM_6 = [
    [CORNER_UP_LEFT, HALF_LEFT],
    [CORNER_UP_LEFT, CORNER_UP_RIGHT],
    [CORNER_DOWN_LEFT, CORNER_DOWN_RIGHT],
]

NUM_7 = [
    [HALF_RIGHT, CORNER_UP_RIGHT],
    [VOID, CORNER_UP_RIGHT],
    [VOID, HALF_UP],
]

NUM_8 = [
    [CORNER_UP_LEFT, CORNER_UP_RIGHT],
    [CORNER_UP_LEFT, CORNER_DOWN_RIGHT],
    [CORNER_DOWN_LEFT, CORNER_DOWN_RIGHT],
]

NUM_9 = [
    [CORNER_UP_LEFT, CORNER_UP_RIGHT],
    [CORNER_DOWN_LEFT, CORNER_DOWN_RIGHT],
    [VOID, HALF_UP],
]



NUMBERS = [
    NUM_0,
    NUM_1,
    NUM_2,
    NUM_3,
    NUM_4,
    NUM_5,
    NUM_6,
    NUM_7,
    NUM_8,
    NUM_9
]

###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################




'''
TO DO:
    - modo rotacion (para anim) vs modo ir a target
    - definir estados concretos para reloj
'''
class Clock:
    def __init__(self,x,y,r, state=[0,0]):
        self.x = x
        self.y = y
        self.r = r
        self.state = state # dos angulos
        self.target = [45, -45]


    def SetTarget(self, target):
        self.target = target + []


    def Update(self):
        if(self.state != self.target):
            new_state = self.state + []
            for i in range(2):
                diff = self.target[i] - self.state[i]
                if(diff != 0):
                    new_state[i] += 1 if diff > 0 else -1
                    # print('moves: ', self.target, self.state)
            self.state = new_state + []
        return


    def Draw(self, pantalla):
        for ang in self.state:
            end = [0,0]
            end[0] = self.x + self.r * np.cos(np.deg2rad(ang))
            end[1] = self.y + self.r * np.sin(np.deg2rad(ang))
            pygame.draw.line(pantalla, (0,0,0), [self.x, self.y], end, 5)


###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################



class ClockSquared:
    def __init__(self, pos):
        self.tam = [9,3]
        self.pos = pos
        self.time = [0,1,2,3]

    def SetTime(self, time):
        self.time = time
        
    
    def GetStates(self, absPos):
        ''' Gets state for clock in absPos'''
        if(absPos[0] == 4):
            return VOID
        
        # pos of number
        relativePos = [
            absPos[0]%2, 
            absPos[1]-self.pos[1]
        ] 

        if(absPos[0] <= 3):
            if(0 <= absPos[0] <= 1):
                number_pos = 0
            elif(2 <= absPos[0] <= 3):
                number_pos = 1
        else:
            if(5 <= absPos[0] <= 6):
                number_pos = 2
            elif(7 <= absPos[0] <= 8):
                number_pos = 3
            
            relativePos[0] = (absPos[0]+1)%2
                
               
                
        number = self.time[number_pos]
        return NUMBERS[number][relativePos[1]][relativePos[0]]
        
        