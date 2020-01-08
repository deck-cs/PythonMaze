import ModelMazeGenerator
import ModelMazeSolver
import time
import sys
import threading
import concurrent.futures as conFu
import MazeException


class MazeModel:
    def __init__(self, amount, size):
        sys.setrecursionlimit(10000)
        self.amount = amount
        self.size = size
        self.solvedTimesList = []
        self.pvList = []
        self.maze = {}
        self.threadsMax = 3
        self.unsolvedMazes = []
        self.lock = threading.Lock()
        self.pvLock = threading.Lock()
        self.mazes = []
        if (self.amount < 1):
            raise Exception("There must be at least be made one maze pr. size")
        print("Made Controller")

    def makeMaze(self): #Is not in use
        try:
            mazeGen = ModelMazeGenerator.MazeGenerator(self.size, self.size)
        except MazeException.MazeException as e: raise
        maze = mazeGen.make_empty_maze()
        maze = mazeGen.genMaze(maze, (0, 0))
        # Sets lower right corner to goal
        maze[len(self.maze)-1][len(maze)-2] = '2'
        maze[0][1] = '0'  # Sets upper left wallpoint to start
        return maze
        # printToFile(maze)
        # readFromFile()

    def solveMaze(self): #Is not in use
        startTime = time.time()  # Initiates the time method
        mazeSolver = ModelMazeSolver.MazeSolver(self.maze)
        mazeSolver.search(0, 1, self.maze, startTime)
        self.pvList.append(mazeSolver.pv)
        self.solvedTimesList.append(mazeSolver.solvedTimes)

    def makeAndSolve(self): #Is not in use
        mazes = []
        for _ in range(self.amount):
            self.maze = self.makeMaze()
            self.solveMaze()
            mazes.append(self.maze)
        print('Finished making mazes size %dx%d' % (self.size, self.size))
        return mazes

    def threadedMakeAndSolve(self):
        print("Starting with threads")
        with conFu.ThreadPoolExecutor(max_workers=self.threadsMax) as executor:
            for _ in range(self.amount):
                try:
                    executor.map(self.makeMazeThread())
                except Exception as e: raise
            for _ in range(self.amount):
                executor.map(self.solveMazeThread())
        return self.mazes

    def makeMazeThread(self):
        print("Making maze")
        try:
            mazeGen = ModelMazeGenerator.MazeGenerator(self.size, self.size)
        except Exception as e: raise
        maze = mazeGen.make_empty_maze()
        maze = mazeGen.genMaze(maze, (0, 0))
        # Sets lower right corner to goal
        maze[len(self.maze)-1][len(maze)-2] = '2'
        maze[0][1] = '0'  # Sets upper left wallpoint to start
        self.lock.acquire()
        self.unsolvedMazes.append(maze)
        self.lock.release()
        print("Finished generating")
        return maze
        # printToFile(maze)
        # readFromFile()

    def solveMazeThread(self):
        print("starting solve")
        self.lock.acquire()
        maze = self.unsolvedMazes[len(self.unsolvedMazes)-1]
        del self.unsolvedMazes[len(self.unsolvedMazes)-1]
        self.lock.release()
        startTime = time.time()  # Initiates the time method
        mazeSolver = ModelMazeSolver.MazeSolver(maze)
        mazeSolver.search(0, 1, maze, startTime)
        self.pvLock.acquire()
        self.pvList.append(mazeSolver.pv)
        self.solvedTimesList.append(mazeSolver.solvedTimes)
        self.mazes.append(maze)
        self.pvLock.release()
        print("Finished solve")
