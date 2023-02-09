import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_169_solution import Solution

class Test(unittest.TestCase):

    def test_example_1(self):
        solution = Solution()
        nums = [3,2,3]
        expected_output = 3
        actual_output = solution.majorityElement(nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2]
        expected_output = 2
        actual_output = solution.majorityElement(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2,3,3,3,3,3]
        expected_output = 3
        actual_output = solution.majorityElement(nums)
        self.assertEqual(actual_output, expected_output)

###################################
if __name__ == '__main__':
    unittest.main()
