import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_39_depth_first import Solution as Solution1
from solutions.leetcode_39_breadth_first import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        inputs = (
            [2,3,6,7],
            7
        )
        expected_output = [[2,2,3],[7]]

        actual_output = self.solution1.combinationSum(*inputs)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.combinationSum(*inputs)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_2(self):
        inputs = (
            [2,3,5],
            8
        )
        expected_output = [[2,2,2,2],[2,3,3],[3,5]]

        actual_output = self.solution1.combinationSum(*inputs)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.combinationSum(*inputs)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_3(self):
        inputs = (
            [2],
            1
        )
        expected_output = []

        actual_output = self.solution1.combinationSum(*inputs)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.combinationSum(*inputs)
        self.assertCountEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()

'''
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
'''