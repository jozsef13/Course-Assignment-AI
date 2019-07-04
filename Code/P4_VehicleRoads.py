from search import *
from utils import *

class VehicleRoads(Problem):
    """n vehicles occupy squares (1, 1) = 0 through (n, 1) = gridSize*(gridSize-1) (i.e., the bottom row) of
    an n×n n grid. The vehicles must be moved to the top row but in reverse
    order; so the vehicle i that starts in (i, 1) = gridSize*i must end up in (n−i+1, n) = n^2-initial state of the vehicle-1. 
    On each time step, every one of the n vehicles can move one square up, down,
    left, or right, or stay put; but if a vehicle stays put, one other adjacent
    vehicle (but not more than one) can hop over it. Two vehicles cannot
    occupy the same square."""

    def __init__(self, gridSize, initial, goal):
        """Define goal state and initial state and initialize the problem"""
        self.gridSize = gridSize
        self.initial = initial
        self.goal = goal
        self.stateIndex = -1 #the index of the position of each vehicle

        Problem.__init__(self, initial, goal)

    def __repr__(self):
        return "< State (%s, %s) >" % (self.initial, self.goal)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only five possible actions
        in any given state of the environment """

        """Calculating the next index of the position for the next vehicle, and if before this, the last vehicle made a move,
        the index will become 0, and start over again with the first vehicle"""
        if self.stateIndex == self.gridSize-1:
            self.stateIndex = 0
        else:
            self.stateIndex = self.stateIndex + 1
        
        possibleActions = ['UP' + str(self.stateIndex), 'DOWN' + str(self.stateIndex), 'LEFT' + str(self.stateIndex), 'RIGHT' + str(self.stateIndex), 'PUT' + str(self.stateIndex)]

        positionVehicle = state[self.stateIndex]
        """Verify the directions our vehicle can move, according to the grid"""
        if positionVehicle < self.gridSize:
            if 'UP' + str(self.stateIndex) in possibleActions:
                possibleActions.remove('UP' + str(self.stateIndex))
        if positionVehicle >= self.gridSize * (self.gridSize - 1):
            if 'DOWN' + str(self.stateIndex) in possibleActions:
                possibleActions.remove('DOWN' + str(self.stateIndex))
        if positionVehicle % self.gridSize == 0:
            if 'LEFT' + str(self.stateIndex) in possibleActions:
                possibleActions.remove('LEFT' + str(self.stateIndex))
        if positionVehicle % self.gridSize == self.gridSize - 1:
            if 'RIGHT' + str(self.stateIndex) in possibleActions:
                possibleActions.remove('RIGHT' + str(self.stateIndex))

        i = 0
        """Verify the actions our vehicle can do, according to the other vehicles"""
        while i < self.gridSize:
            positionVehicle1 = state[i]

            if i != self.stateIndex:
                if positionVehicle-self.gridSize == positionVehicle1:
                    if 'UP' + str(self.stateIndex) in possibleActions:
                        possibleActions.remove('UP' + str(self.stateIndex))
                if positionVehicle+self.gridSize == positionVehicle1:
                    if 'DOWN' + str(self.stateIndex) in possibleActions:
                        possibleActions.remove('DOWN' + str(self.stateIndex))
                if positionVehicle-1 == positionVehicle1:
                    if 'LEFT' + str(self.stateIndex) in possibleActions:
                        possibleActions.remove('LEFT' + str(self.stateIndex))
                if positionVehicle+1 == positionVehicle1:
                    if 'RIGHT' + str(self.stateIndex) in possibleActions:
                        possibleActions.remove('RIGHT' + str(self.stateIndex))
            
            i = i + 1

        return possibleActions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        positionVehicle = state[self.stateIndex]
        newState = list(state)

        delta = {'UP'+ str(self.stateIndex):-self.gridSize, 'DOWN'+ str(self.stateIndex):+self.gridSize, 'LEFT'+ str(self.stateIndex):-1, 'RIGHT'+ str(self.stateIndex):+1, 'PUT' + str(self.stateIndex):+0}
        newState[self.stateIndex] = positionVehicle + delta[action]
        return tuple(newState)
    
    def goal_state(self, state):
         """ Given a state, return True if state is a goal state or False, otherwise """
        
         return state == self.goal

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = Manhattan Distance """
        manhattanDistance = sum(abs(s-g)*2 for (s, g) in zip(node.state, self.goal))
        return manhattanDistance
