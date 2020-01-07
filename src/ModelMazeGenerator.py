from random import shuffle
import MazeException

class MazeGenerator:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        if(sizeX <= 0 or sizeY <= 0):
            mazEx = MazeException.MazeException()
            mazEx.mazeMess("Invalid size input.")
            raise mazEx
        self.maze = self.make_empty_maze()

    # Makes an array, that can be interpreted maze with no walls
    def make_empty_maze(self):
        try:
            # Makes an empty array, in a list, within a list(2D bruh)
            maze = [[[] for b in range(self.sizeX)] for a in range(self.sizeY)]
            return maze
        except IndexError:
            print("Error: can\'t make the maze")

    def convert(self, maze):
        pretty_maze = [["1"]*(2*len(maze[0])+1) for a in range(2*len(maze)+1)]
        for y, row in enumerate(maze):
            for x, col in enumerate(row):
                pretty_maze[2*y+1][2*x+1] = "0"
                for direction in col:
                    pretty_maze[2*y+1+direction[0]][2*x+1+direction[1]] = "0"
        return pretty_maze

    # Generates and returns a maze

    def genMaze(self, maze, coords=(0, 0)):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        shuffle(directions)     # Randomizes direction list
        for direction in directions:  # Goes through the list of directions
            new_coords = (coords[0] + direction[0], coords[1] + direction[1])
            if (0 <= new_coords[0] < len(maze)) and \
                (0 <= new_coords[1] < len(maze[0])) and \
                    not maze[new_coords[0]][new_coords[1]]:  # Checks if next space is within maze walls and if visited prior
                # Appends upcoming direction for current space
                maze[coords[0]][coords[1]].append(direction)
                maze[new_coords[0]][new_coords[1]].append(
                    (-direction[0], -direction[1]))  # Appends direction it came from, for future space
                self.genMaze(maze, new_coords)  # Recursively calls itself to move on
        maze = self.convert(maze)
        return maze
