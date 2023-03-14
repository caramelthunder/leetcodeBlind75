import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_17_backtracking import Solution as Solution1
from solutions.leetcode_17_str_concat import Solution as Solution2


class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        digits = "23"
        expected_output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        actual_output = self.solution1.letterCombinations(digits)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.letterCombinations(digits)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_2(self):
        digits = ""
        expected_output = []

        actual_output = self.solution1.letterCombinations(digits)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.letterCombinations(digits)
        self.assertCountEqual(actual_output, expected_output)
    
    def test_example_3(self):
        digits = "2"
        expected_output = ["a","b","c"]

        actual_output = self.solution1.letterCombinations(digits)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.letterCombinations(digits)
        self.assertCountEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()