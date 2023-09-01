import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_270_iterative import Solution as iterative_solution
from solutions.leetcode_270_recursive import Solution as recursive_solution
from helpers.leetcode_270_helper import TreeHelpers


class Test(unittest.TestCase):
    def setUp(self):
        self.recursive_closest_value = recursive_solution().closestValue
        self.iterative_closest_value = iterative_solution().closestValue
        self.arr_to_tree = TreeHelpers().arr_to_tree

    def test_01(self):
        root, target = self.arr_to_tree([4, 2, 5, 1, 3]), 3.714286
        expected = 4

        actual_recursive = self.recursive_closest_value(root, target)
        self.assertEqual(actual_recursive, expected)

        actual_iterative = self.iterative_closest_value(root, target)
        self.assertEqual(actual_iterative, expected)

    def test_02(self):
        root, target = self.arr_to_tree([1]), 4.428571
        expected = 1

        actual_recursive = self.recursive_closest_value(root, target)
        self.assertEqual(actual_recursive, expected)

        actual_iterative = self.iterative_closest_value(root, target)
        self.assertEqual(actual_iterative, expected)

    def test_03(self):
        root, target = self.arr_to_tree([5, 10, 15]), 4
        expected = 5

        actual_recursive = self.recursive_closest_value(root, target)
        self.assertEqual(actual_recursive, expected)

        actual_iterative = self.iterative_closest_value(root, target)
        self.assertEqual(actual_iterative, expected)


######################################
if __name__ == "__main__":
    unittest.main()
