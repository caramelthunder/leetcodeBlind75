import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_42_monotonic_stack import Solution as Solution1
from solutions.leetcode_42_two_scans_dynamic_programming import (
    Solution as Solution2,
)
from solutions.leetcode_42_two_pointers import Solution as Solution3


class Test(unittest.TestCase):
    def setUp(self):
        self.using_stack = Solution1()
        self.using_dp = Solution2()
        self.using_two_pointers = Solution3()

    def test_example_1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected_output = 6

        actual_output = self.using_stack.trap(height=height)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.using_dp.trap(height=height)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.using_two_pointers.trap(height=height)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        height = [4, 2, 0, 3, 2, 5]
        expected_output = 9

        actual_output = self.using_stack.trap(height=height)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.using_dp.trap(height=height)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.using_two_pointers.trap(height=height)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
