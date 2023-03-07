import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_54_solution import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected_output = [1,2,3,6,9,8,7,4,5]

        actual_output = self.solution.spiralOrder(matrix)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected_output = [1,2,3,4,8,12,11,10,9,5,6,7]

        actual_output = self.solution.spiralOrder(matrix)
        self.assertEqual(actual_output, expected_output)



######################################
if __name__ == '__main__':
    unittest.main()