import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_56_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected_output = [[1,6],[8,10],[15,18]]

        actual_output = self.solution.merge(intervals)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_2(self):
        intervals = [[1,4],[4,5]]
        expected_output = [[1,5]]

        actual_output = self.solution.merge(intervals)
        self.assertCountEqual(actual_output, expected_output)
    
    def test_no_overlap(self):
        intervals = [[1,2],[4,5],[7,8]]
        expected_output = [[1,2],[4,5],[7,8]]

        actual_output = self.solution.merge(intervals)
        self.assertCountEqual(actual_output, expected_output)

    def test_all_overlap(self):
        intervals = [[1,5],[2,6],[3,8],[4,7]]
        expected_output = [[1,8]]

        actual_output = self.solution.merge(intervals)
        self.assertCountEqual(actual_output, expected_output)

    def test_some_overlap(self):
        intervals = [[1,3],[2,4],[5,7],[6,8]]
        expected_output = [[1,4],[5,8]]

        actual_output = self.solution.merge(intervals)
        self.assertCountEqual(actual_output, expected_output)

    def test_single_interval(self):
        intervals = [[1,5]]
        expected_output = [[1,5]]

        actual_output = self.solution.merge(intervals)
        self.assertCountEqual(actual_output, expected_output)

    def test_empty_list(self):
        intervals = []
        expected_output = []

        actual_output = self.solution.merge(intervals)
        self.assertCountEqual(actual_output, expected_output)
        
######################################
if __name__ == '__main__':
    unittest.main()


'''
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''