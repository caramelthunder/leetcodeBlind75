import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_298_solution import Solution
from helpers.leetcode_298_helper import TreeHelpers


class Test(unittest.TestCase):
    def setUp(self):
        self.longest_consectutive = Solution().longestConsecutive
        self.arr_to_tree = TreeHelpers().arr_to_tree

    def test_1(self):
        root = self.arr_to_tree(
            [
                1,
                None,
                3,
                None,
                None,
                2,
                4,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                5,
            ]
        )
        expected_output = 3

        actual_output = self.longest_consectutive(root)
        self.assertEqual(actual_output, expected_output)

    def test_2(self):
        root = self.arr_to_tree(
            [
                2,
                None,
                3,
                None,
                None,
                2,
                None,
                None,
                None,
                None,
                None,
                1,
                None,
                None,
                None,
                None,
                None,
            ]
        )
        expected_output = 2

        actual_output = self.longest_consectutive(root)
        self.assertEqual(actual_output, expected_output)

    def test_3(self):
        root = self.arr_to_tree(
            [1, 2, 3, 4, 5, None, None, None, None, None, None]
        )
        expected_output = 2

        actual_output = self.longest_consectutive(root)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
