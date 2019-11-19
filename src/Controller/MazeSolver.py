import time
class MazeSolver:
    def __init__(self, maze):  # also add solved methods when ready
        self.maze = maze

        self.solvedTimesList = []

    def search(self, x, y, maze, startTime):
        global pv
        if maze[x][y] == '2':
            print('found at %d,%d' % (x, y))
            end = time.time()
            print(
                '\n'.join([''.join(['{:4}'.format(item) for item in row])for row in maze]))
            # print('\n'.join([''.join(['{:4}'.format(item) for item in row])
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
        if ((x < len(maze)-1 and self.search(x+1, y, maze, startTime))
            or (y > 0 and self.search(x, y-1, maze, startTime))
            or (x > 0 and self.search(x-1, y, maze, startTime))
                or (y < len(maze)-1 and self.search(x, y+1, maze, startTime))):
            return True
        return False
