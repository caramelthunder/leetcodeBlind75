import sys
import os
import unittest
import copy

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_994_solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        grid = [[2,1,1],
                [1,1,0],
                [0,1,1]]
        expected_output = 4

        actual_output = self.solution.orangesRotting(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        grid = [[2,1,1],
                [0,1,1],
                [1,0,1]]
        expected_output = -1

        actual_output = self.solution.orangesRotting(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        grid = [[0,2]]
        expected_output = 0

        actual_output = self.solution.orangesRotting(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)
    
    def test_multiple_rottens_at_start(self):
        grid = [[2,1,1],
                [1,1,0],
                [0,1,2]]
        expected_output = 2

        actual_output = self.solution.orangesRotting(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)
    
    def test_empty(self):
        grid = [[0]]
        expected_output = 0

        actual_output = self.solution.orangesRotting(copy.deepcopy(grid))
        self.assertEqual(actual_output, expected_output)
        


######################################
if __name__ == '__main__':
    unittest.main()
