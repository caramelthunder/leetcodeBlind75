import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_226_helper import TreeHelper
from solutions.leetcode_226_iterative import Solution as Solution1
from solutions.leetcode_226_recursive import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.helper = TreeHelper()
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example1(self):
        params = [4,2,7,1,3,6,9]
        expected_output = [4,7,2,9,6,3,1]

        actual_output1 = self.helper.tree_to_numbers(self.solution1.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.helper.tree_to_numbers(self.solution2.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output2, expected_output)

    def test_example2(self):
        params = [2,1,3]
        expected_output = [2,3,1]

        actual_output1 = self.helper.tree_to_numbers(self.solution1.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.helper.tree_to_numbers(self.solution2.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output2, expected_output)

    def test_example3(self):
        params = []
        expected_output = []

        actual_output1 = self.helper.tree_to_numbers(self.solution1.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.helper.tree_to_numbers(self.solution2.invertTree(self.helper.numbers_to_tree(params)))
        self.assertEqual(actual_output2, expected_output)

#################################
if __name__ == '__main__':
    unittest.main()

