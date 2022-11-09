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
    return result

if __name__ == '__main__':
    
    random.seed(7) #To make reproducible
    frame = line(0,0,0,1,30) | line(30,0,0,1,30) | line(0,0,1,0,30) | line(0,30,1,0,31)
    
    
    problem = GridProblem(initial=(6,4), goal=(16,25), obstacles=random_lines(X=range(27), Y=range(27), N=25, lengths=range(1,6)) | frame)
    solution_breadth_first = breadth_first_graph_search(problem)
    problem.plot_grid_problem(solution_breadth_first, 'Breadth search')
    solution_depth_first = depth_first_graph_search(problem)
    problem.plot_grid_problem(solution_depth_first, 'Depth search')
    solution_uniform_cost = uniform_cost_search(problem)
    problem.plot_grid_problem(solution_uniform_cost, 'Uniform search')
    
    print("FIN")