import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1143_memoisation import Solution as Solution1
from solutions.leetcode_1143_tabulation import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        text1, text2 = "abcde", "ace"
        expected_output = 3

        actual_output = self.solution1.longestCommonSubsequence(text1, text2)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonSubsequence(text1, text2)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        text1, text2 = "abc", "abc"
        expected_output = 3

        actual_output = self.solution1.longestCommonSubsequence(text1, text2)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonSubsequence(text1, text2)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        text1, text2 = "abc", "def"
        expected_output = 0

        actual_output = self.solution1.longestCommonSubsequence(text1, text2)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonSubsequence(text1, text2)
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        text1, text2 = "bsbininm", "jmjkbkjkv"
        expected_output = 1

        actual_output = self.solution1.longestCommonSubsequence(text1, text2)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.longestCommonSubsequence(text1, text2)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()