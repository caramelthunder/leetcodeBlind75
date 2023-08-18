import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_84_solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        heights = [2, 1, 5, 6, 2, 3]
        expected_output = 10
        actual_output = self.solution.largestRectangleArea(heights)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        heights = [2, 4]
        expected_output = 4
        actual_output = self.solution.largestRectangleArea(heights)
        self.assertEqual(actual_output, expected_output)

    def test_descending_order(self):
        heights = [5, 4, 3, 2, 1]
        expected_output = 9
        actual_output = self.solution.largestRectangleArea(heights)
        self.assertEqual(actual_output, expected_output)

    def test_ascending_order(self):
        heights = [1, 2, 3, 4, 5]
        expected_output = 9
        actual_output = self.solution.largestRectangleArea(heights)
        self.assertEqual(actual_output, expected_output)

    def test_equal_heights(self):
        heights = [3, 3, 3, 3, 3]
        expected_output = 15
        actual_output = self.solution.largestRectangleArea(heights)
        self.assertEqual(actual_output, expected_output)

    def test_single_height(self):
        heights = [7]
        expected_output = 7
        actual_output = self.solution.largestRectangleArea(heights)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_peaks(self):
        heights = [2, 1, 4, 5, 1, 3, 3]
        expected_output = 8
        actual_output = self.solution.largestRectangleArea(heights)
        self.assertEqual(actual_output, expected_output)

    def test_empty_input(self):
        heights = []
        expected_output = 0
        actual_output = self.solution.largestRectangleArea(heights)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
