import time
class MazeSolver:
    def __init__(self, maze):  # also add solved methods when ready
        self.maze = maze
        self.solvedTimes = 0
        self.pv = 0

    def search(self, x, y, maze, startTime):
        if maze[x][y] == '2':
            #print('found at %d,%d' % (x, y))
            end = time.time()
            #print(    '\n'.join([''.join(['{:4}'.format(item) for item in row])for row in maze]))
            # print('\n'.join([''.join(['{:4}'.format(item) for item in row])
            #                 for row in maze]))
            timeUsed = end - startTime
            #print("Time used:" + " " + str((timeUsed)))
            self.solvedTimes = timeUsed
            return True
        elif maze[x][y] == '1':
            #print('wall at %d,%d' % (x, y))
            return False
        elif maze[x][y] == '3':
            #print('visited at %d,%d' % (x, y))
            self.pv += 1
            return False

        #print('visiting %d,%d' % (x, y))

        # mark as visited

        maze[x][y] = '3'
        self.pv += 1
        # explore neighbors clockwise starting by the one on the right - This is where recursive functions use the boolean values to check which way it can move
        if ((x < len(maze)-1 and self.search(x+1, y, maze, startTime)) #Looks down, and checks if out of bounds.
            or (y < len(maze)-1 and self.search(x, y+1, maze, startTime)) #Looks to the right, and checks if out of bounds.
            or (x > 0 and self.search(x, y-1, maze, startTime)) #Looks to the left
                or (y > 0 and self.search(x-1, y, maze, startTime))): #Looks up
            return True
        maze[x][y]='4'
        return False
