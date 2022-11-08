'''
It creates a grid search problem based on Problem class from the AIMA-python source code of
the book Artificial Ingellligence A Modern Approach. 

The grid search problem will be resolve by search algorithms.

Created on 8 nov 2022

@author: Euegnio Martínez Cámara
'''

from search import *
from enum import Enum, unique

import heuristics
from django.db.migrations import state

@unique
class Directions(Enum):
 
    UP=(0,1),
    DOWN=(0,-1),
    RIGHT=(1,0),
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
        
        self.__directions = [Directions.DOWN, Directions.UP, Directions.RIGHT, Directions.LEFT]

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
        next_states = {}
        for k in self.__directions.keys():
            next_states.add(x + self.__directions[k][0], y + self.__directions[k][1])
        
        #It is a difference among sets. All the possible actions except the obstacles.
        
        return  next_states - self.obstacles


    def result(self, state, action):
        return action if action not in self.obstacles else state


    def goal_test(self, state):
        return Problem.goal_test(self, state)


    def path_cost(self, c, state1, action, state2):
        return Problem.path_cost(self, c, state1, action, state2)


    def value(self, state):
        return Problem.value(self, state)

        