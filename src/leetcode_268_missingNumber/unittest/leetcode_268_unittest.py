import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_268_naive_sort import Solution as Solution1
from solutions.leetcode_268_better_hash_table import Solution as Solution2
from solutions.leetcode_268_optimized import Solution as Solution3

class Test(unittest.TestCase):
    def setUp(self):
        self.naive_solution= Solution1()
        self.better_solution= Solution2()
        self.optimized_solution = Solution3()
    
    def test_example_1(self):
        nums = [3,0,1]
        expected_output = 2
        
        actual_output = self.naive_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.better_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimized_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [0,1]
        expected_output = 2

        actual_output = self.naive_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.better_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimized_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        nums = [9,6,4,2,3,5,7,0,1]
        expected_output = 8

        actual_output = self.naive_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.better_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimized_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_4(self):
        nums = [9,6,4,2,3,5,7,8,1]
        expected_output = 0

        actual_output = self.naive_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.better_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.optimized_solution.missingNumber(nums=nums)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()
