import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_487_sliding_window import Solution as SlidingWindow
from solutions.leetcode_487_prefix_sum import Solution as PrefixSum


class Test(unittest.TestCase):
    def setUp(self):
        self.sliding_window = SlidingWindow()
        self.prefix_sum = PrefixSum()

    def test_example_1(self):
        nums = [1, 0, 1, 1, 0]
        expected_output = 4

        actual_output = self.sliding_window.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.prefix_sum.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [1, 1, 0, 1]
        expected_output = 4

        actual_output = self.sliding_window.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.prefix_sum.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

    def test_all_ones(self):
        nums = [1, 1, 1, 1, 1]
        expected_output = 5

        actual_output = self.sliding_window.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.prefix_sum.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        expected_output = 1

        actual_output = self.sliding_window.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.prefix_sum.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

    def test_alternating_nums(self):
        nums = [0, 1, 0, 1, 0, 1]
        expected_output = 3

        actual_output = self.sliding_window.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.prefix_sum.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

    def test_single_element_1(self):
        nums = [1]
        expected_output = 1

        actual_output = self.sliding_window.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.prefix_sum.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

    def test_single_element_0(self):
        nums = [0]
        expected_output = 1

        actual_output = self.sliding_window.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.prefix_sum.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_zeros_in_the_middle(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1]
        expected_output = 4

        actual_output = self.sliding_window.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.prefix_sum.findMaxConsecutiveOnes(nums)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
