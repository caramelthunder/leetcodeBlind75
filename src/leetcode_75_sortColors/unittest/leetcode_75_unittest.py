import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_75_solution import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [2,0,2,1,1,0]
        expected_output = [0,0,1,1,2,2]

        actual_output = self.solution.sortColors(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [2,0,1]
        expected_output = [0,1,2]

        actual_output = self.solution.sortColors(nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        nums = [2,0,2,1,0,1]
        expected_output = [0,0,1,1,2,2]

        actual_output = self.solution.sortColors(nums)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()