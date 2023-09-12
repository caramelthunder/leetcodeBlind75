import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_490_breadth_first import Solution as BreadthFirst
from solutions.leetcode_490_depth_first import Solution as DepthFirst


class Test(unittest.TestCase):
    def setUp(self):
        self.breadth_first = BreadthFirst()
        self.depth_first = DepthFirst()

    def test_example_1(self):
        maze = [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        start = [0, 4]
        destination = [4, 4]

        self.assertTrue(self.breadth_first.hasPath(maze, start, destination))
        self.assertTrue(self.depth_first.hasPath(maze, start, destination))

    def test_example_2(self):
        maze = [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        start = [0, 4]
        destination = [3, 2]

        self.assertFalse(self.breadth_first.hasPath(maze, start, destination))
        self.assertFalse(self.depth_first.hasPath(maze, start, destination))

    def test_example_3(self):
        maze = [
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 0, 0],
        ]
        start = [4, 3]
        destination = [0, 1]

        self.assertFalse(self.breadth_first.hasPath(maze, start, destination))
        self.assertFalse(self.depth_first.hasPath(maze, start, destination))


######################################
if __name__ == "__main__":
    unittest.main()
