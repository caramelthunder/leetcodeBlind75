import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_57_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        input = (
            [[1,3],[6,9]],  # intervals
            [2,5]           # newInterval
        )
        expected_output = [[1,5],[6,9]]
        actual_output = self.solution.insert(*input)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        input = (
            [[1,2],[3,5],[6,7],[8,10],[12,16]],     # intervals
            [4,8]                                   # newInterval
        )
        expected_output = [[1,2],[3,10],[12,16]]
        actual_output = self.solution.insert(*input)
        self.assertEqual(actual_output, expected_output)

    def test_empty_intervals(self):
        input = (
            [], # intervals
            [0, 10] # newInterval
        )
        expected_output = [[0, 10]]
        actual_output = self.solution.insert(*input)
        self.assertEqual(actual_output, expected_output)

    def test_new_interval_at_beginning(self):
        input = (
            [[5, 10], [20, 25]], # intervals
            [0, 4] # newInterval
        )
        expected_output = [[0, 4], [5, 10], [20, 25]]
        actual_output = self.solution.insert(*input)
        self.assertEqual(actual_output, expected_output)

    def test_new_interval_at_end(self):
        input = (
            [[5, 10], [20, 25]], # intervals
            [30, 35] # newInterval
        )
        expected_output = [[5, 10], [20, 25], [30, 35]]
        actual_output = self.solution.insert(*input)
        self.assertEqual(actual_output, expected_output)

    def test_complete_overlap(self):
        input = (
            [[5, 10], [20, 25], [30, 35]], # intervals
            [0, 40] # newInterval
        )
        expected_output = [[0, 40]]
        actual_output = self.solution.insert(*input)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_overlaps(self):
        input = (
            [[5, 10], [20, 25], [30, 35], [40, 45]], # intervals
            [15, 35] # newInterval
        )
        expected_output = [[5, 10], [15, 35], [40, 45]]
        actual_output = self.solution.insert(*input)
        self.assertEqual(actual_output, expected_output)

    def test_no_overlaps(self):
        input = (
            [[5, 10], [20, 25], [30, 35]], # intervals
            [12, 18] # newInterval
        )
        expected_output = [[5, 10], [12, 18], [20, 25], [30, 35]]
        actual_output = self.solution.insert(*input)
        self.assertEqual(actual_output, expected_output)


#########################################
if __name__ == '__main__':
    unittest.main()