import MazeGenerator
import MazeSolver
import time
import sys


class MazeController:
    def __init__(self, amount, size):
        sys.setrecursionlimit(10000)
        self.amount = amount
        self.size = size
        self.solvedTimesList = []
        self.pvList = []

    def makeMaze(self, size):
        mazeGen = MazeGenerator.MazeGenerator(size, size)
        maze = mazeGen.genMaze((0, 0))
        maze[len(maze)-1][len(maze)-2] = '2'  # Sets lower right corner to goal
        maze[0][1] = '0'  # Sets upper left wallpoint to start
        # printToFile(maze)
        # readFromFile()

    def solveMaze(self, maze):
        startTime = time.time()  # Initiates the time method
        mazeSolver = MazeSolver.MazeSolver(maze)
        mazeSolver.search(0, 1, maze, startTime)
        self.pvList.append(mazeSolver.pv)
