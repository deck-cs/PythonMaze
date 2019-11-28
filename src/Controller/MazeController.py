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
        self.maze = {}
        print("Made Controller")

    def makeMaze(self):
        mazeGen = MazeGenerator.MazeGenerator(self.size, self.size)
        maze = mazeGen.make_empty_maze()
        maze = mazeGen.genMaze(maze,(0, 0))
        maze[len(self.maze)-1][len(maze)-2] = '2'  # Sets lower right corner to goal
        maze[0][1] = '0'  # Sets upper left wallpoint to start
        return maze
        # printToFile(maze)
        # readFromFile()

    def solveMaze(self):
        startTime = time.time()  # Initiates the time method
        mazeSolver = MazeSolver.MazeSolver(self.maze)
        mazeSolver.search(0, 1, self.maze, startTime)
        self.pvList.append(mazeSolver.pv)
        self.solvedTimesList.append(mazeSolver.solvedTimes)

    def makeAndSolve(self):
        for _ in range(self.amount):
            self.maze = self.makeMaze()
            self.solveMaze()
        print('Finished making mazes size %dx%d' %(self.size,self.size))
