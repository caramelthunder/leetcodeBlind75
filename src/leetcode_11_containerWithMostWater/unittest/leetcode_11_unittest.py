import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_11_solution import Solution

class Test(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        height = [1,8,6,2,5,4,8,3,7]
        expected_output = 49

        actual_output = self.solution.maxArea(height)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        height = [1,1]
        expected_output = 1

        actual_output = self.solution.maxArea(height)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()