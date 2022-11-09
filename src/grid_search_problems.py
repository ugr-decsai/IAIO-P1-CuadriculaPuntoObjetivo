'''
It creates a grid search problem based on Problem class from the AIMA-python source code of
the book Artificial Ingellligence A Modern Approach. 

The grid search problem will be resolve by search algorithms.

Created on 8 nov 2022

@author: Euegnio Martínez Cámara
'''

from search import *
from enum import Enum, unique

import matplotlib.pyplot as plt
import heuristics
import math
import utils4e


@unique
class Directions(Enum):
 
    UP=(0,1)
    DOWN=(0,-1)
    RIGHT=(1,0)
    LEFT=(-1,0)


class GridProblem(Problem):
    '''
    classdocs
    '''


    def __init__(self, initial=None, goal=None, obstacles=(), **kwds):
        '''
        Constructor
        '''
        Problem.__init__(self, initial, goal=goal,
                         obstacles=set(obstacles) - {initial, goal}, **kwds)
        
        self.__directions = [Directions.__members__[k].value for k in Directions.__members__.keys()]
        self.__failure = Node('FALLO', path_cost=math.inf) #Nodo que indica que
                        #indica que el algoritmo no encuentra solución al problema
        self.__cutoff = Node('INTERRUMPIDO', path_cost=math.inf) #Nodo que indica
                    #que el algoritmo de búsqueda en profundidad se ha
                        #interrumpido.
    def is_goal(self, state):
        return Problem.is_goal(self, state)

                        

    def action_cost(self, s, a, s1):
        return heuristics.straight_line_distance(s, s1)


    def h(self, node):
        return heuristics.straight_line_distance(node.state, self.goal)


    def actions(self, state):
        """All the actions that can do
        
        state:
            The current state (it is a node).
            
        Returns:
            A dictionary with the following positions.
        """
        #inline: {(x + self.__directions.__members__[k],y + self.__directions.__members__[k])[1]for k in self.__directions.__members__.keys()}
        x, y = state
        next_states = set()
        for d in self.__directions:
            next_states.add((x + d[0], y + d[1]))
        
        #It is a difference among sets. All the possible actions except the obstacles.
        
        return  next_states - self.obstacles


    def result(self, state, action):
        return action if action not in self.obstacles else state



    def path_cost(self, c, state1, action, state2):
        return Problem.path_cost(self, c, state1, action, state2)


    def value(self, state):
        return Problem.value(self, state)
    
    def plot_grid_problem(self, solution, title='Search', show=True):
        """It plots a grid problem.
        
        Args:
            grid:
            solution:
            reached:
            title:
            show: Boolean value that determines whether the plot must be showed
            or not.
        
        """
        plt.figure(figsize=(16, 10))
        plt.axis('off')
        plt.axis('equal')
        plt.scatter(*transpose(self.obstacles), marker='s', color='darkgrey')
        plt.scatter(*transpose(self.explored), marker='.', c='blue')
        plt.scatter(*transpose(solution.path_states()), marker='s', c='blue')
        plt.scatter(*transpose([self.initial]), 9**2, marker='D', c='green')
        plt.scatter(*transpose([self.goal]), 9**2, marker='D', c='red')
        if show: plt.show()
        print('{} {} search: {:.1f} path cost, {:,d} states reached'
          .format(' ' * 10, title, solution.path_cost, len(self.explored)))
        

        