import unittest
import Controller.MazeSolver
import Controller.MazeGenerator as mG


class solveMazeTest(unittest.TestCase):
    #Tror den mangler en init?

    def test_placeVisited(self):
        maze = mG.MazeGenerator.genMaze()


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()