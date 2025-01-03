from piezas import *
from colorama import Fore, Style, Back
import mysql.connector
import hashlib
import os
import pandas as pd

db_config = {
    'user': 'miquel',
    'password': 'patata',
    'host': 'localhost',
    'database': 'chess_db',
}

DISK_DB_PATH = 'db/data.json'

INITIAL_STATE = [
    ['tn','cn','an','qn','kn','an','cn','tn'],
    ['pn','pn','pn','.','pn','pn','pn','pn'],
    [ '.', '.', '.', '.', '.', '.', '.', '.'],
    [ '.', '.', '.', '.', '.', '.', '.', '.'],
    [ '.', '.', '.', '.', '.', '.', '.', '.'],
    [ '.', '.', '.', '.', '.', '.', '.', '.'],
    ['pb','pb','pb','pb','pb','pb','pb','pb'],
    ['tb','cb','ab','qb','kb','ab','cb','tb'],
]

class DB:
    def __init__(self, mode):
        self.mode = mode
        self.df = None
        
    def check_if_saved():
        return False
    
    def save_to_disk(self, row):
        if(self.df is None):
            self.df = pd.read_json(DISK_DB_PATH, orient='records')
        self.df = pd.concat([self.df, pd.DataFrame([row])], ignore_index=True)
        self.df.to_json(DISK_DB_PATH, orient='records', indent=4)
        
    def get_from_disk(self, id):
        if(self.df is None):
            self.df = pd.read_json(DISK_DB_PATH, orient='records')
        row = self.df.loc[self.df['id'] == id]
        return row.to_dict(orient='records')[0] if not row.empty else None

    
    def save_to_db(self):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        insert_query = "INSERT INTO boards (id, pos_value, best_move, board_state, turn) VALUES (%s, %s, %s, %s, %s)"
        data = (
            self.get_hash(), 
            2, 
            3, 
            self.get_board_string(), 
            0 if self.turno == BLANCO else 1
        )
        cursor.execute(insert_query, data)
        connection.commit()
        
        cursor.close()
        connection.close()
        return
    
    def get_from_db(self):
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM boards WHERE id=%s",(self.get_hash(),))
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        connection.close()
        return
    
class Tablero:
    def __init__(self, state=None):
        self.turno = BLANCO
        self.state = state
        self.tablero = [[None for j in range(8)] for i in range(8)]
        self.board_string = ''
        self.hash = -1
        
        self.available_spaces = []
        self.available_pieces = []
        self.selected = []
        self.last_move = []
        self.killed = {BLANCO:[],NEGRO:[]}
        
        self.db = DB(mode='disk')
        if(state is None):
            self.state = INITIAL_STATE+[]
    
        for i in range(8):
            for j in range(8):
                if(self.state[i][j] != '.'):
                    self.tablero[i][j] = EQUIVALENCIAS[self.state[i][j][0]](i,j,self.state[i][j][1])
    
        self.get_available_pieces()
    
    def coord_to_pos(self, coord):
        pos = []
        pos.append(8-int(coord[1]))
        pos.append(ord(coord[0])-97)
        return pos
        
    def __str__(self):
        cadena = ''
        cadena += f'{Fore.BLACK}{Style.DIM}   a b c d e f g h \n'
        
        for i, row in enumerate(self.tablero):
            cadena += F'{Fore.BLACK}{Style.DIM} {str(8-i)}{Style.NORMAL} '
            # printea una fila
            for j, item in enumerate(row):
                
                if([i,j] == self.selected):
                    cadena += Back.RED + item.print_piece() + Back.RESET
                    
                elif([i,j] in self.available_spaces):
                    if(item is None):
                        if([i,j] in self.last_move):
                            cadena += f'{Back.LIGHTGREEN_EX}{Fore.RED}X{Back.RESET}'
                        else:
                            cadena += f'{Fore.RED}x'
                    else:
                        cadena += Back.RED+item.print_piece()+Back.RESET
                        
                elif(item is not None):
                    if([i,j] in self.last_move):
                        cadena += f'{Back.LIGHTGREEN_EX}{Fore.BLACK}{item.print_piece()}{Back.RESET}'
                    else:
                        cadena += item.print_piece()
                    
                else:
                    if([i,j] in self.last_move):
                        cadena += f'{Back.LIGHTGREEN_EX}{Fore.BLACK}.{Back.RESET}'
                    else:
                        cadena += f'{Fore.BLACK}.'
                    
                cadena += ' '
            
            cadena += f'{Fore.BLACK}\t|\t'
            
            if(i==0):
                cadena += Fore.BLUE
                cadena += ' '.join([x.print_piece() for x in self.killed[NEGRO]])
            
            if(i==7):
                cadena += Fore.YELLOW
                cadena += ' '.join([x.print_piece() for x in self.killed[BLANCO]])
                   
            cadena += '\n'
            
        return cadena
    
    def get_available_moves(self, pos):
        pos = self.coord_to_pos(pos)
        if(pos in self.available_pieces):
            self.available_spaces = self.tablero[pos[0]][pos[1]].get_available_spaces(self.state)
            self.selected = pos + []
    
    def move(self, pos):
        pos = self.coord_to_pos(pos)
        if(pos in self.available_spaces):
            # si mata, la guarda
            if(self.state[pos[0]][pos[1]] != '.'):
                if(self.turno == BLANCO):
                    self.killed[NEGRO].append(self.tablero[pos[0]][pos[1]])
                else:
                    self.killed[BLANCO].append(self.tablero[pos[0]][pos[1]])
                    
            # mueve la pieza
            self.tablero[pos[0]][pos[1]] = self.tablero[self.selected[0]][self.selected[1]]
            self.state[pos[0]][pos[1]] = self.state[self.selected[0]][self.selected[1]]
            self.tablero[self.selected[0]][self.selected[1]] = None
            self.state[self.selected[0]][self.selected[1]] = '.'
            
            # actualiza mas cosas
            # TODO: actualizar puntuacion
            # TODO: comprobar hakes y mates
            self.tablero[pos[0]][pos[1]].move(pos)
            self.last_move = [self.selected, pos]
            self.selected = []
            self.available_spaces = []
            self.turno = BLANCO if self.turno==NEGRO else NEGRO
            self.get_available_pieces()
        return
    
    def get_available_pieces(self):
        self.available_pieces = []
        for i in range(8):
            for j in range(8):
                if(self.state[i][j] != '.' and self.state[i][j][1]==self.turno):
                    self.available_pieces.append([i,j])
        return
    
    
    def get_board_string(self):
        if(self.board_string == ''):
            for row in self.state:
                for pos in row:
                    self.board_string += pos + ' '
        return self.board_string
    
    def get_hash(self):
        if(self.hash == -1):
            sha256_hash = hashlib.sha256()
            sha256_hash.update((self.turno + self.get_board_string()).encode('utf-8'))
            self.hash = sha256_hash.hexdigest()
        return self.hash
    
    def check_if_saved(self):
        return self.db.check_if_saved()
    
    def save_position(self):
        data = {
            'id': self.get_hash(),
            'turn': 0 if self.turno == BLANCO else 1,
            'pos_value': -1, 
            'best_move': "", 
            'board_state':self.get_board_string(), 
        }
        return self.db.save_to_disk(data)
        
    def get_position(self, id=None):
        if(id is None):
            id = self.get_hash()
        return self.db.get_from_disk(id)
    
    
if(__name__=="__main__"):
    tabl = Tablero()
    print(tabl)
    print(tabl.get_hash())
    id = tabl.save_position()
    print(tabl.get_position(id))
