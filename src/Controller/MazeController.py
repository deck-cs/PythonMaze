import MazeGenerator
import MazeSolver
import time


class MazeController:
    def __init__(self, amount, size):
        self.amount = amount
        self.size = size
        self.solvedTimesList = []

    def makeMaze(self, size):

        mazeGen = MazeGenerator.MazeGenerator(size, size)

        maze = mazeGen.genMaze((0, 0))

        maze[len(maze)-1][len(maze)-2] = '2'  # Sets lower right corner to goal
        maze[0][1] = '0'  # Sets upper left wallpoint to start
        startTime = time.time()  # Initiates the time method
        mazeSolver = MazeSolver.MazeSolver(maze)
        mazeSolver.search(0, 1, maze, startTime)
        pvList.append(pv)
        print("places visited = " + str(pv))
        # printToFile(maze)
        # readFromFile()
