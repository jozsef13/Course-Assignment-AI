import time
import search
from P4_VehicleRoads import *
from InputDataGenerator import *

def main():

    gridSize = generateGridSize()
    initialState = generateInitialState(gridSize)
    goalState = generateGoalState(gridSize, initialState)
    print("The size of the grid is:", gridSize, "\n")
    print("The initial state:", initialState, "\n")
    print("The goal state:", goalState, "\n")
    problem_p4VehicleRoads = VehicleRoads(gridSize, initialState, goalState)
    t1 = time.time()
    problem_p4VehicleRoadsSol = search.astar_search(problem_p4VehicleRoads, problem_p4VehicleRoads.h)
    t2 = time.time()
    print("Path:", problem_p4VehicleRoadsSol.solution(), "\nTime:", t2-t1, "\n")

if __name__ == "__main__":
    main()

