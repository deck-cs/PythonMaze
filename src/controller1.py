import sys
import time
from random import randint, shuffle, choice
import matplotlib.pyplot as plt


# needed for DFS...
sys.setrecursionlimit(10000)
pv = 0                  # PlaceVisited
pvList = []             # List of how many places was visited
solvingTimes = []       # Contains solvetimes for current iteration of puzzles, paired with specific attempt. Eg. 5x5 or 10x10 puzzles.
solvedTimesList = []    # Min, avg and max times for current iteration.
relatedValues = []      # List of time/placesVisited
theTimes= []            # The values of solvingTimes listed
tryList = []            # The keys of solvingTimes listed
pvListFinal = []        # Min, avg and max values of pvList for export
iteration = 0    #The maze size of the current iteration

    # This method resets global values back to default

def prefab():
    sys.setrecursionlimit(10000)
    global pv
    pv = 0
    global solvedTimesList
    solvedTimesList = []
    global pvList 
    pvList = []
    global solvingTimes
    solvingTimes = []

# Each maze cell contains a tuple of directions of cells to which it is connected
# Takes a maze and converts it to an array of 1's and 0's to represent walls, etc


def convert(maze):
    pretty_maze = [["1"]*(2*len(maze[0])+1) for a in range(2*len(maze)+1)]
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            pretty_maze[2*y+1][2*x+1] = "0"
            for direction in col:
                pretty_maze[2*y+1+direction[0]][2*x+1+direction[1]] = "0"
    return pretty_maze

# Takes a converted maze and pretty prints it


def pretty(maze):
    for a in convert(maze):
        string = ""
        for b in a:
            string += b
        print(string)
    print("")

# Returns an empty maze of given size
#Beneath will be exported to MazeGenerator

def make_empty_maze(width, height):
    try:
        maze = [[[] for b in range(width)] for a in range(height)]  #Makes an empty array, in a list, within a list(2D bruh)
        return maze
    except IndexError:
        print("Error: can\'t make the maze")

# Recursive backtracker.
# Looks at its neighbors randomly, if unvisitied, visit and recurse

# Beneath will be exported to MazeGenerator

def DFS(maze, coords=(0, 0)):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    shuffle(directions)     # Randomizes direction list
    for direction in directions:    #Goes through the list of directions
        new_coords = (coords[0] + direction[0], coords[1] + direction[1])
        if (0 <= new_coords[0] < len(maze)) and \
           (0 <= new_coords[1] < len(maze[0])) and \
           not maze[new_coords[0]][new_coords[1]]:      #Checks if next space is within maze walls and if visited prior (Can it trap itself here?)
            maze[coords[0]][coords[1]].append(direction) #Appends upcoming direction for current space
            maze[new_coords[0]][new_coords[1]].append(
                (-direction[0], -direction[1])) #Appends direction it came from, for future space
            DFS(maze, new_coords)   #Recursively calls itself to move on
    return maze


def search(x, y, maze, startTime):
    global pv
    if maze[x][y] == '2':
        print('found at %d,%d' % (x, y))
        end = time.time()
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in maze]))
        #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
        #                 for row in maze]))
        timeUsed = end - startTime
        print("Time used:" + " " + str((timeUsed)))
        solvedTimesList.append(timeUsed)
        return True
    elif maze[x][y] == '1':
        print('wall at %d,%d' % (x, y))
        return False
    elif maze[x][y] == '3':
        print('visited at %d,%d' % (x, y))
        pv += 1
        return False

    print('visiting %d,%d' % (x, y))

    # mark as visited

    maze[x][y] = '3'
    pv += 1
    # explore neighbors clockwise starting by the one on the right - This is where recursive functions use the boolean values to check which way it can move
    if ((x < len(maze)-1 and search(x+1, y, maze, startTime))
        or (y > 0 and search(x, y-1, maze, startTime))
        or (x > 0 and search(x-1, y, maze, startTime))
            or (y < len(maze)-1 and search(x, y+1, maze, startTime))):
        return True
    return False


##################### Read and print to file #####################

# 'r'  Read mode which is used when the file is only being read
# 'w'  Write mode which is used to edit and write new information to the file(any existing files with the same name will be erased when this mode is activated)
# 'a'  Appending mode, which is used to add new data to the end of the file that is new information is automatically amended to the end
# 'r+' Special read and write mode, which is used to handle both actions when working with a file

nameOfFile = "testfile.txt"


def printToFile(mazeToPrint):
    print("Writing til file")
    try:
        file = open("testfile.txt", "w+")
        try:
            print("Printing to file")
            file.write(str("places visited = " + str(pv)))
            file.write(str(mazeToPrint))
        finally:
            print("Going to close the file - WRITE")
            file.close()
    except IOError:
        print("Error: can\'t find file or read data")


def readFromFile():
    print("Reading from file")
    try:
        file = open("testfile.txt", "r")
        try:
            print("Reading the file testfile.txt")
            print(file.readlines())
        finally:
            print("Going to close the file - READ")
            file.close()
    except IOError:
        print("Error: can\'t find file or read data")

################### Read and print to file END ##################


def makeMazeAndSolve(size):
    maze = DFS(make_empty_maze(size, size), (0, 0))
    maze = convert(maze)
    maze[len(maze)-1][len(maze)-2] = '2' #Sets lower right corner to goal
    maze[0][1] = '0'    #Sets upper left wallpoint to start
    startTime = time.time()    #Initiates the time method
    search(0, 1, maze, startTime)
    pvList.append(pv)
    print("places visited = " + str(pv))
    printToFile(maze)
    readFromFile()
    return maze

def mainRun(size):
    global iteration
    iteration = size
    prefab()
    for x in range(10): #number of MakeAndSolves
        global pv
        pv = 0
        makeMazeAndSolve(size) #input is size


    print(solvedTimesList)
    print(pvList)

# Setting keys on the solvedTimesList(just for working with the x-axis)


def makeStatNumbers():
    global solvingTimes
    global relatedValues
    solvingTimes = {}
    x = 1
    for aTry in solvedTimesList:
        solvingTimes.setdefault(x, 0)
        solvingTimes[x] = aTry
        x+=1
# Splitting the keys and the values up into lists
def getStatKeys():
    global tryList
    global iteration
    min = "min"
    min+=str(iteration)
    avg = "avg"
    avg+=str(iteration)
    max = "max"
    max+= str(iteration)
    tryList.append(min)
    tryList.append(avg)
    tryList.append(max)
    return tryList

def getStatValues():
    global theTimes
    theTimes.append(min(list(solvingTimes.values())))
    theTimes.append(sum(list(solvingTimes.values()))/len(list(solvingTimes.values())))
    theTimes.append(max(list(solvingTimes.values())))
    return theTimes

def getRelatedValues():
    global relatedValues
    solveList = list(solvingTimes.values())
    minKey = min(solvingTimes, key=solvingTimes.get)-1
    relatedValues.append(min(solveList)/pvList[minKey])

    relatedValues.append((sum(solveList)/len(solveList))/((sum(pvList)/len(pvList))))

    maxKey = max(solvingTimes, key=solvingTimes.get)-1
    relatedValues.append(min(solveList)/pvList[maxKey])

def getPvListFinal():
    global pvListFinal
    pvListFinal.append(min(pvList))
    pvListFinal.append(sum(pvList)/len(pvList))
    pvListFinal.append(max(pvList))
# Splitting the keys and the values up into lists
