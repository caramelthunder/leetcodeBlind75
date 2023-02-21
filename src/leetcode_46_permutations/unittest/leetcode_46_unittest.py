import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_46_array_insertion import Solution as Solution1
from solutions.leetcode_46_backtracking import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        nums = [1,2,3]
        expected_output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        actual_output = self.solution1.permute(nums)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.permute(nums)
        self.assertCountEqual(actual_output, expected_output)
    
    def test_example_2(self):
        nums = [0,1]
        expected_output = [[0,1],[1,0]]

        actual_output = self.solution1.permute(nums)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.permute(nums)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_3(self):
        nums = [1]
        expected_output = [[1]]

        actual_output = self.solution1.permute(nums)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.permute(nums)
        self.assertCountEqual(actual_output, expected_output)



######################################
if __name__ == '__main__':
    unittest.main()


'''
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
'''