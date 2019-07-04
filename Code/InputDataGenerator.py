import random

def generateGridSize():
    """Generate the size of the grid"""
    return random.randint(1,5)

def generateInitialState(gridSize):
    """Generate the initial state with the start position for each vehicle, which is the first column of a matrix,
    but each position i, j from matrix is denoted with numbers starting from 0 till the gridSize like this, if i = 1
    and j = 1, the position will be 0, for i = 1 and j = 2, the position will be 1, and so on till the last position,
     which will be equal with the number of gridSize variable"""
    initialState = tuple()

    i = 0
    while i < gridSize:
        initialState = initialState + tuple([gridSize*i])
        i = i + 1
       
    return initialState

def generateGoalState(gridSize, initialState):
    """Generate the goal state, with the same idea as above, but with another formula, because, each vehicle has to reach 
    the position with the coordinates n-i+1,n so for me, it has to reach, n^2-initial state of the vehicle-1, this means
    that it has to reach the top row, but in reverse order"""
    goalState = tuple()

    i = 0
    while i < gridSize:
        goalState = goalState + tuple([(gridSize**2)-initialState[i]-1])
        i = i + 1

    return goalState