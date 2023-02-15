import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_238_solution import Solution as Solution1
from solutions.leetcode_238_solution_space_optimized import Solution as Solution2


class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        nums = [1,2,3,4]
        expected_output = [24,12,8,6]

        actual_output = self.solution1.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [-1,1,0,-3,3]
        expected_output = [0,0,9,0,0]

        actual_output = self.solution1.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_short_array(self):
        nums = [2, 3]
        expected_output = [3, 2]

        actual_output = self.solution1.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

    def test_zero_elements(self):
        nums = []
        expected_output = []

        actual_output = self.solution1.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

    def test_single_element(self):
        nums = [5]
        expected_output = [1]

        actual_output = self.solution1.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

    def test_negative_elements(self):
        nums = [-2, -3, 4, -5]
        expected_output = [60, 40, -30, 24]

        actual_output = self.solution1.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

    def test_duplicate_elements(self):
        nums = [2, 2, 2, 2]
        expected_output = [8, 8, 8, 8]

        actual_output = self.solution1.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

#####################################
if __name__ == '__main__':
    unittest.main()