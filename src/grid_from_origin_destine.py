'''
Created on 8 nov. 2022

@author: Eugenio Martínez Cámara
'''

import random
from search import *
from grid_search_problems import GridProblem


def line(x, y, dx, dy, length):
    """A line of `length` cells starting at (x, y) and going in (dx, dy) direction.
    
    Args:
        x: It is an integer with the coordinate x of the first point of the line.
        y: It is an integer with the coordinate y of the first point of the line.
        dx:
        dy:
        length: Number of cells.
    """
    
    return {(x + i*dx, y + i*dy) for i in range(length)}
    
    
def random_lines(X, Y, N, lengths):
    result=set()
    for _ in range(N):
        x, y = random.choice(X), random.choice(Y)
        dx, dy = random.choice(((0,1), (1,0)))
        result |= line(x, y, dx, dy, random.choice(lengths))

if __name__ == '__main__':
    
    random.seed(7) #To make reproducible
    frame = line(0,5,0,1,20) | line(30,5,1,0,20)
    
    
    problem = GridProblem(initial=(6,4), goal=(10,22), obstacles=random_lines(X=range(31), Y=(31), N=20, lengths=range(1,5)))
    solution = breadth_first_tree_search(problem)