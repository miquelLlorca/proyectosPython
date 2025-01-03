import random
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import numpy as np


def shuffle(deck, height, stack_number):
    stacks = [[] for i in range(stack_number)]
    
    for i in range(stack_number):
        for j in range(height):
            stacks[i].append(deck[stack_number*j+i])
    
    for i in range(stack_number):
        if 1 in stacks[i]:
            pos = i
            break

    zr = []
    for i in range(height):
        zr.append(0)
    
    #! REVISAR como poner en la mitad el monton
    if pos == 2:
        stacks.pop(0)
        stacks.append(zr)
    elif pos == 0:
        stacks.pop(2)
        stacks.insert(0, zr)

    return stacks

def search_card(deck):
    for i in range(len(deck)):
        if(deck[i] == 1):
            return i+1





def get_pos_matrix(height, stack_number):
    deck = []
    pos_matrix = []
    for pos in range(stack_number*height):
        pos_matrix.append([pos])
        deck = []
        for i in range(stack_number*height):
            deck.append(1 if i==pos else 0)

        i=0
        while(True):
            stacks = shuffle(deck, height, stack_number)
            deck = []
            for stack in stacks:
                for card in stack:
                    deck.append(card)
            pos_matrix[pos].append(search_card(deck))

            i += 1
            if(pos_matrix[pos][i] == pos_matrix[pos][i-1]):
                pos_matrix[pos].pop(i)
                break
    return pos_matrix


def plot_pos_matrix(pos_matrix):       
    x = []
    for i in range(len(pos_matrix[0])):
        x.append(i)

    for i in range(3*height):
        while(len(pos_matrix[i]) < len(pos_matrix[0])):
            pos_matrix[i].append((3*height)/2 + 0.5)
            
        plt.plot(x, pos_matrix[i])

    plt.show()
    plt.savefig(f'/home/miquel/proyectosPython/random/truco_magia/{len(pos_matrix)}_cards.png')
    
    


def plot_distribution(number_of_iters):
    plt.plot(
        np.linspace(start=1, stop=len(number_of_iters)*2, num=len(number_of_iters)),
        number_of_iters
    )
    plt.show()
    plt.savefig('/home/miquel/proyectosPython/random/truco_magia/distribution.png')
    

def get_distribution():
    height = 1
    stack_number = 3
    number_of_iters = []
    for i in tqdm(range(1, 1000, 2)):
        number_of_iters.append(
            len(get_pos_matrix(i, stack_number)[0])-1
        )
    plot_distribution(number_of_iters)
        
if(__name__ == "__main__"):
    # get_distribution()
    with open('/home/miquel/proyectosPython/random/truco_magia/results.txt','r') as file:
        data = file.read().split('-')
    print(data)
    for i, item in enumerate(data):
        if(item != data[i+1]):
            print(f'Step at {i+1}, from {item} to {data[i+1]}')
            
            
# Step at 1, from 1 to 2
# Step at 2, from 2 to 3
# Step at 5, from 3 to 4
# Step at 14, from 4 to 5
# Step at 41, from 5 to 6
# Step at 122, from 6 to 7
# Step at 365, from 7 to 8