from random import shuffle

class MazeGenerator:
    def __init__(self, sizeX, sizeY, generatorType,):
        self.coords = (0,0)
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.generatorType = generatorType
        self. maze = {}

    #Makes an array, that can be interpreted maze with no walls
    def make_empty_maze(self):
        try:
            maze = [[[] for b in range(self.sizeX)] for a in range(self.sizeY)]  #Makes an empty array, in a list, within a list(2D bruh)
            return maze
        except IndexError:
            print("Error: can\'t make the maze")

    #Generates and returns a maze
    def genMaze(self, coords=(0, 0)):
        maze = self.make_empty_maze()
        coords = self.coords
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
                self.genMaze(new_coords)   #Recursively calls itself to move on
        return maze
