import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_368_top_down_memoisation import Solution as Solution1
from solutions.leetcode_368_bottom_up_tabulation import Solution as Solution2


class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        nums = [1,2,3]
        expected_output = [[1,2] ,[1,3]]

        actual_output = self.solution1.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)

    def test_example_2(self):
        nums = [1,2,4,8]
        expected_output = [[1,2,4,8]]

        actual_output = self.solution1.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)
    
    def test_example_3(self):
        nums = [8,9,4,2,12,1,3]
        expected_output = [[1,2,4,8], [1,2,4,12]]

        actual_output = self.solution1.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)

    def test_example_4(self):
        nums = [125,1,8,3,24,9,18,2,4,25,12,72]
        expected_output = [[1,2,4,8,24,72], [1,2,4,12,24,72]]

        actual_output = self.solution1.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)
    
    def test_example_5(self):
        nums = [1]
        expected_output = [[1]]

        actual_output = self.solution1.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.largestDivisibleSubset(nums)
        self.assertIn(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()