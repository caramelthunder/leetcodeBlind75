import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_14_solution_vertical_scan import Solution as Solution1
from solutions.leetcode_14_solution_horizontal_scan import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        strs = ["flower","flow","flight"]
        expected_output = "fl"

        actual_output = self.solution1.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        strs = ["dog","racecar","car"]
        expected_output = ""

        actual_output = self.solution1.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        strs = ["ab", "abc", "abcd", "abcde"]
        expected_output = "ab"

        actual_output = self.solution1.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        strs = ["", "a", "ab"]
        expected_output = ""

        actual_output = self.solution1.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

    def test_example_5(self):
        strs = ["same", "same", "same"]
        expected_output = "same"

        actual_output = self.solution1.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonPrefix(strs)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()