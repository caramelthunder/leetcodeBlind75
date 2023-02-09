import unittest
import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_53_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected_output = 6
        actual_output = self.solution.maxSubArray(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example2(self):
        nums = [1]
        expected_output = 1
        actual_output = self.solution.maxSubArray(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example3(self):
        nums = [5,4,-1,7,8]
        expected_output = 23
        actual_output = self.solution.maxSubArray(nums)
        self.assertEqual(actual_output, expected_output)

    def test_all_negative(self):
        nums = [-5, -10, -15, -20]
        expected_output = -5
        actual_output = self.solution.maxSubArray(nums)
        self.assertEqual(actual_output, expected_output)

#############################
if __name__ == '__main__':
    unittest.main()