import unittest
import Controller_MazeController as mCon
import Controller_MazeGenerator as mG
import Controller_SubController as sCon
import os.path


class TestSum(unittest.TestCase):

    def test_makeEmptyMaze(self):
        mazeGen = mG.MazeGenerator(5, 5)
        emptyMaze = mazeGen.make_empty_maze()
        self.assertEqual(len(emptyMaze), 5, "Checks the length of the array")

    def test_makeMaze(self):
        mc = mCon.MazeController(1, 5)
        maze = mc.makeMaze()
        self.assertEqual(maze[0][1], '0', "Checking for start of maze")
        self.assertEqual(maze[10][9], '2', "Checking for end of maze")

    def test_solveMaze(self):
        for _ in range(10):  # running this test multiple times because of its random nature
            mc = mCon.MazeController(1, 5)
            maze = mc.makeMaze()
            mc.maze = maze
            mc.solveMaze()
            self.assertEqual(
                maze[9][9], '3', "Checking if it has found the exit")

    def test_saveToJSON(self):
        mc = mCon.MazeController(1, 5)
        maze = mc.makeMaze()
        sc = sCon.SubController(1, 5)
        sc.mazesArray = maze
        sc.saveToJSON("test")
        self.assertTrue(os.path.isfile('test.json'),
                        "Checking if the file has been created")
        os.remove('test.json')  # deleting the file again

    def test_loadFromJSON(self):
        mc = mCon.MazeController(1, 5)
        maze = mc.makeMaze()
        sc = sCon.SubController(1, 5)
        sc.mazesArray = maze
        sc.saveToJSON("test")
        sc.mazesArray = []
        sc.loadFromJSON("test")
        self.assertEqual(
            sc.mazesArray[0][1], '0', "Checking that the maze exists and has a start")
        os.remove('test.json')  # deleting the file again


if __name__ == '__main__':
    unittest.main()
