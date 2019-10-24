import sys
import time
from random import randint, shuffle, choice
import matplotlib.pyplot as plt


# needed for DFS...
sys.setrecursionlimit(10000)
pv = 0
solvedTimesList = []
pvList = []
solvingTimes = []
relatedValues = []
theTimes= []
tryList = []

def prefab():
    sys.setrecursionlimit(10000)
    pv = 0
    solvedTimesList = []
    pvList = []
    solvingTimes = {}
    relatedValues = {}
    theTimes= {}
    tryList = {}

# Each maze cell contains a tuple of directions of cells to which it is connected

# Takes a maze and converts it to an array of X's and blanks to represent walls, etc


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


def make_empty_maze(width, height):
    maze = [[[] for b in range(width)] for a in range(height)]
    return maze

# Recursive backtracker.
# Looks at its neighbors randomly, if unvisitied, visit and recurse


def DFS(maze, coords=(0, 0)):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    shuffle(directions)
    for direction in directions:
        new_coords = (coords[0] + direction[0], coords[1] + direction[1])
        if (0 <= new_coords[0] < len(maze)) and \
           (0 <= new_coords[1] < len(maze[0])) and \
           not maze[new_coords[0]][new_coords[1]]:
            maze[coords[0]][coords[1]].append(direction)
            maze[new_coords[0]][new_coords[1]].append(
                (-direction[0], -direction[1]))
            DFS(maze, new_coords)
    return maze


def search(x, y, maze, start):
    global pv
    if maze[x][y] == '2':
        print('found at %d,%d' % (x, y))
        end = time.time()
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in maze]))
        #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
        #                 for row in maze]))
        timeUsed = end - start
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
    # explore neighbors clockwise starting by the one on the right-
    if ((x < len(maze)-1 and search(x+1, y, maze, start))
        or (y > 0 and search(x, y-1, maze, start))
        or (x > 0 and search(x-1, y, maze, start))
            or (y < len(maze)-1 and search(x, y+1, maze, start))):
        return True
    return False


##################### Print to file #####################

def printToFile(mazeToPrint):
    file = open("testfile.txt", "w")

    file.write(str(mazeToPrint))
    # file.write("This is our new text file")
    # file.write("and this is another line.")
    # file.write("Why? Because we can.")

    file.close()


def makeMazeAndSolve(size):
    maze = DFS(make_empty_maze(size, size), (0, 0))
    maze = convert(maze)
    maze[len(maze)-1][len(maze)-2] = '2'
    maze[0][1] = '0'
    start = time.time()
    search(0, 1, maze, start)
    pvList.append(pv)
    print("places visited = " + str(pv))
    printToFile(maze)

def mainRun():
    for x in range(50):
        global pv
        pv = 0
        makeMazeAndSolve(5)


    print(solvedTimesList)
    print(pvList)

# Setting keys on the solvedTimesList(just for working with the x-axis)

def makeStatNumbers():
    global solvingTimes
    global relatedValues
    solvingTimes = {}
    x = 1
    for aTry in solvedTimesList:
        solvingTimes.setdefault(x,0)
        solvingTimes[x] = aTry
        x+=1
    relatedValues = {}
    y = 0
    for interval in solvingTimes:
        relatedValues.setdefault(y,0)
        relatedValues[y] = getStatValues()[y]/getStatKeys()[y]
        y+=1

# Splitting the keys and the values up into lists
def getStatKeys():
    global tryList
    tryList = list(solvingTimes.keys())
    return tryList

#solvingTimes = makeStatNumbers()
def getStatValues():
    global theTimes
    theTimes = list(solvingTimes.values())
    return theTimes

def getRelatedValues():
    global relatedValues
    relatedValues = list(relatedValues.values())
