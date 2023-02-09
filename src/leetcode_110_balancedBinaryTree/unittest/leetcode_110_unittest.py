import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_110_solution import Solution
from helpers.leetcode_110_helper import Helper

class Test(unittest.TestCase):
    def setUp(self):
       self.solution = Solution()
       self.helper = Helper()
    
    def test_example_1(self):
        nums = [3,9,20,'null','null',15,7]
        expected_output = True
        actual_output = self.solution.isBalanced(
            self.helper.nums_to_tree(nums)
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [1,2,2,3,3,'null','null',4,4]
        expected_output = False
        actual_output = self.solution.isBalanced(
            self.helper.nums_to_tree(nums)
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        nums = []
        expected_output = True
        actual_output = self.solution.isBalanced(
            self.helper.nums_to_tree(nums)
        )
        self.assertEqual(actual_output, expected_output)

################################
if __name__ == '__main__':
    unittest.main()
