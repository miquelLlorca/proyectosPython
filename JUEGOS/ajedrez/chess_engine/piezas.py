from colorama import Fore

BLANCO = 'b'
NEGRO = 'n'

IMAGENES ={
    NEGRO:{
        'c':'c',
        'a':'a',
        't':'t',
        'p':'p',
        'k':'k',
        'q':'q',
    },
    BLANCO:{
        'c':'c',
        'a':'a',
        't':'t',
        'p':'p',
        'k':'k',
        'q':'q',
    }
}

INCORRECT_POS = -1
EMPTY_SPACE = 0
OTHER_COLOR = 1
SAME_COLOR = 2

def check_pos(x, y, color, state):
    # TODO: falta tener en cuenta el color
    pos_correcta = ((0 <= x <= 7) and (0 <= y <= 7))
    if(not pos_correcta):
        return INCORRECT_POS
    
    hay_pieza = (state[x][y]!='.')
    if(not hay_pieza):
        return EMPTY_SPACE
    
    mismo_color = (color == state[x][y][1])
    if(mismo_color):
        return SAME_COLOR
    return OTHER_COLOR

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

class Pieza:
    def __init__(self, x, y, color, tipo):
        self.x = x
        self.y = y
        self.image = IMAGENES[color][tipo]
        self.tipo = tipo
        self.color = color
        self.char = '@' 

    def get_available_spaces(self):
        return
    
    def move(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        
    def draw_piece(self, pantalla):
        # blit img
        return
    
    def print_piece(self):
        color = Fore.YELLOW if self.color==BLANCO else Fore.BLUE
        return f'{color}{self.char}'
        
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

class Caballo(Pieza):
    
    def __init__(self, x, y, color):
        self.tipo = 'c'
        super().__init__(x, y, color, self.tipo)
        self.char = 'L' 
    
    def get_available_spaces(self, state):
        spaces = []
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if(abs(i) != abs(j)):
                    new_x = i + self.x
                    new_y = j + self.y
                    check = check_pos(new_x, new_y, self.color, state)
                    if(check == EMPTY_SPACE or check == OTHER_COLOR):
                        spaces.append([new_x, new_y])
        return spaces
    
    def move(self, pos):
        super().move(pos)
        
    def draw_piece(self, pantalla):
        super().draw_piece(pantalla)
        
    def print_piece(self):
        return super().print_piece()

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

class Alfil(Pieza):
    
    def __init__(self, x, y, color):
        self.tipo = 'a'
        super().__init__(x, y, color, self.tipo)
        self.char = '&' 
    
    def get_available_spaces(self, state):
        spaces = []
        dirs = [
            [ 1, 1], [-1, 1], [ 1,-1], [-1,-1]
        ]
        for dir in dirs:
            step = 1
            stop = False
            while(not stop):
                i = self.x + dir[0]*step
                j = self.y + dir[1]*step
                check = check_pos(i, j, self.color, state)
                if(check == EMPTY_SPACE):
                    spaces.append([i,j])
                elif(check == OTHER_COLOR):
                    spaces.append([i,j])
                    stop = True
                elif(check == INCORRECT_POS or check == SAME_COLOR):
                    stop = True
                step += 1
        return spaces
    
    def move(self, pos):
        super().move(pos)
        
    def draw_piece(self, pantalla):
        super().draw_piece(pantalla)
        
    def print_piece(self):
        return super().print_piece()

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

class Torre(Pieza):
    
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 't')
        self.char = '#' 
    
    def get_available_spaces(self, state):
        spaces = []
        dirs = [
            [ 1, 0], [-1, 0], [ 0, 1], [ 0,-1]
        ]
        for dir in dirs:
            step = 1
            stop = False
            while(not stop):
                i = self.x + dir[0]*step
                j = self.y + dir[1]*step
                check = check_pos(i, j, self.color, state)
                if(check == EMPTY_SPACE):
                    spaces.append([i,j])
                elif(check == OTHER_COLOR):
                    spaces.append([i,j])
                    stop = True
                elif(check == INCORRECT_POS or check == SAME_COLOR):
                    stop = True
                step += 1
        return spaces
    
    def move(self, pos):
        super().move(pos)
        
    def draw_piece(self, pantalla):
        super().draw_piece(pantalla)
        
    def print_piece(self):
        return super().print_piece()

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

class Peon(Pieza):
    
    def __init__(self, x, y, color):
        self.tipo = 'p'
        super().__init__(x, y, color, self.tipo)
        self.char = 'i' 
        self.direction = -1 if color==BLANCO else 1
    
    def get_available_spaces(self, state):
        spaces = []
        if(self.x == 1 or self.x == 6):
            new_x = self.x+2*self.direction
            new_y = self.y
            check = check_pos(new_x, new_y, self.color, state)
            if(check == EMPTY_SPACE):
                spaces.append([new_x, new_y])
            
        for j in [-1, 0, 1]:
            new_x = self.x+self.direction
            new_y = self.y+j
            check = check_pos(new_x, new_y, self.color, state)
            if(abs(j)==1 and check == OTHER_COLOR):
                spaces.append([new_x, new_y])
            elif(j==0 and check == EMPTY_SPACE):
                spaces.append([new_x, new_y])
        return spaces
    
    def move(self, pos):
        super().move(pos)
        
    def draw_piece(self, pantalla):
        super().draw_piece(pantalla)
        
    def print_piece(self):
        return super().print_piece()

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

class Rey(Pieza):
    
    def __init__(self, x, y, color):
        self.tipo = 'k'
        super().__init__(x, y, color, self.tipo)
        self.char = 'K' 
    
    def get_available_spaces(self, state):
        spaces = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if(not (i==0 and j==0)):
                    
                    new_x = i + self.x
                    new_y = j + self.y
                    check = check_pos(new_x, new_y, self.color, state)
                    if(check == EMPTY_SPACE or check == OTHER_COLOR):
                        spaces.append([new_x, new_y])
                    #! VERIFICAR HAKE y/o MATE, de momento solo es una pieza mas
        return spaces
    
    
    def move(self, pos):
        super().move(pos)
        
    def draw_piece(self, pantalla):
        super().draw_piece(pantalla)
        
    def print_piece(self):
        return super().print_piece()

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

class Reina(Pieza):
    
    def __init__(self, x, y, color):
        self.tipo = 'q'
        super().__init__(x, y, color, self.tipo)
        self.char = 'Q' 
    
    def get_available_spaces(self, state):
        spaces = []
        dirs = [
            [ 1, 0], [-1, 0], [ 0, 1], [ 0,-1],
            [ 1, 1], [-1, 1], [ 1,-1], [-1,-1]
        ]
        for dir in dirs:
            step = 1
            stop = False
            while(not stop):
                i = self.x + dir[0]*step
                j = self.y + dir[1]*step
                check = check_pos(i, j, self.color, state)
                if(check == EMPTY_SPACE):
                    spaces.append([i,j])
                elif(check == OTHER_COLOR):
                    spaces.append([i,j])
                    stop = True
                elif(check == INCORRECT_POS or check == SAME_COLOR):
                    stop = True
                step += 1
        return spaces
    
    def move(self, pos):
        super().move(pos)
        
    def draw_piece(self, pantalla):
        super().draw_piece(pantalla)
        
    def print_piece(self):
        return super().print_piece()


EQUIVALENCIAS = {
    'c': Caballo,
    'a': Alfil,
    't': Torre,
    'p': Peon,
    'k': Rey,
    'q': Reina,
}