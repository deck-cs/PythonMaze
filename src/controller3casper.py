import sys, time
from random import randint, shuffle, choice
import matplotlib.pyplot as plt


# needed for DFS...
sys.setrecursionlimit(10000)
pv = 0

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


def search(x, y):
    
    global pv
    if maze[x][y] == '2':
        print('found at %d,%d' % (x, y))
        end = time.time()

        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in maze]))
        print("Time used:" + " " + str(end - start))
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
    if ((x < len(maze)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
            or (y < len(maze)-1 and search(x, y+1))):
        return True
    return False


maze = DFS(make_empty_maze(12, 12), (0, 0))
maze = convert(maze)
maze[len(maze)-1][len(maze)-2] = '2'
maze[0][1] = '0'
start = time.time()
search(0, 1)
print("places visited = " + str(pv))

plt.cla()
plt.bar(10, 10 ,width=0.5, align='center') # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
#plt.ticklabel_format(useOffset=False)
plt.axis([0, 0, 100, 100]) #axis(x-min, x-max, y-min, y-max)
plt.title("Test", fontsize=12)
plt.xlabel("Ages", fontsize=10)
plt.ylabel("Amount", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()