'''
Python file for the development of heuristics.

Created on 8 nov. 2022

@author: genimarca
'''




def straight_line_distance(A, B):
    """Calculation of the Euclidena Distance.
    
    args:
        a: point representation as a set with an undefined number of components.
        b: point representation as a set with an undefined number of components.
    return:
        The euclidean distance.
    """
    
    return sum(abs(a-b)**2 for (a, b) in zip(A, B))** 0.5
        