from Controller import MazeGenerator
from Controller import MazeSolver
import time
import sys


class MazeController:
    def __init__(self, amount, size):
        sys.setrecursionlimit(10000)
        self.amount = amount
        self.size = size
        self.solvedTimesList = []
        self.pvList = []
        self.maze = {}
        print("Made Controller")

    def makeMaze(self):
        mazeGen = MazeGenerator.MazeGenerator(self.size, self.size)
        self.maze = mazeGen.make_empty_maze()
        self.maze = mazeGen.genMaze(self.maze,(0, 0))
        self.maze[len(self.maze)-1][len(self.maze)-2] = '2'  # Sets lower right corner to goal
        self.maze[0][1] = '0'  # Sets upper left wallpoint to start
        # printToFile(maze)
        # readFromFile()

    def solveMaze(self):
        startTime = time.time()  # Initiates the time method
        mazeSolver = MazeSolver.MazeSolver(self.maze)
        mazeSolver.search(0, 1, self.maze, startTime)
        self.pvList.append(mazeSolver.pv)
