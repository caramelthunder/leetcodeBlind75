import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_733_DFS import Solution as Solution1
from solutions.leetcode_733_BFS import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.dfs_solution = Solution1()
        self.bfs_solution = Solution2()
    
    def test_example1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr, sc, color = 1, 1, 2
        expected_output = [[2,2,2],[2,2,0],[2,0,1]]

        actual_output_dfs = self.dfs_solution.floodFill(image, sr, sc, color)
        self.assertEqual(actual_output_dfs, expected_output)
        actual_output_bfs = self.bfs_solution.floodFill(image, sr, sc, color)
        self.assertEqual(actual_output_bfs, expected_output)

    def test_example2(self):
        image = [[0,0,0],[0,0,0]]
        sr, sc, color = 0, 0, 0
        expected_output = [[0,0,0],[0,0,0]]

        actual_output_dfs = self.dfs_solution.floodFill(image, sr, sc, color)
        self.assertEqual(actual_output_dfs, expected_output)
        actual_output_bfs = self.bfs_solution.floodFill(image, sr, sc, color)
        self.assertEqual(actual_output_bfs, expected_output)

    def test_empty_grid(self):
        # Test starting pixel at the corner of the grid
        self.assertEqual(self.dfs_solution.floodFill([[0, 1], [1, 1]], 0, 0, 2), [[2, 1], [1, 1]])
        self.assertEqual(self.bfs_solution.floodFill([[0, 1], [1, 1]], 0, 0, 2), [[2, 1], [1, 1]])

    def test_same_color(self):
        self.assertEqual(self.dfs_solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 1), [[1,1,1],[1,1,0],[1,0,1]])
        self.assertEqual(self.bfs_solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 1), [[1,1,1],[1,1,0],[1,0,1]])
        
    #######################################
if __name__ == '__main__':
    unittest.main()