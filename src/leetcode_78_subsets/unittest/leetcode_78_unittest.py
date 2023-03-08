import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_78_backtracking import Solution as Solution1
from solutions.leetcode_78_array_concat import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        nums = [1,2,3]
        expected_output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        actual_output = self.solution1.subsets(nums)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.subsets(nums)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [0]
        expected_output = [[],[0]]

        actual_output = self.solution1.subsets(nums)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.subsets(nums)
        self.assertCountEqual(actual_output, expected_output)




######################################
if __name__ == '__main__':
    unittest.main()