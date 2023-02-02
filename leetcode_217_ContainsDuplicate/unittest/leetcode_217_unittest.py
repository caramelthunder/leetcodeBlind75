import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_217_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1,2,3,1]
        expected_output = True
        actual_output = self.solution.containsDuplicate(nums= nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        nums = [1,2,3,4]
        expected_output = False
        actual_output = self.solution.containsDuplicate(nums= nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        expected_output = True
        actual_output = self.solution.containsDuplicate(nums= nums)
        self.assertEqual(actual_output, expected_output)


###########################
if __name__ == '__main__':
    unittest.main()
    