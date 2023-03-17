import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_438_solution import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s, p = "cbaebabacd", "abc"
        expected_output = [0, 6]
        actual_output = self.solution.findAnagrams(s, p)
        self.assertCountEqual(actual_output, expected_output)
    
    def test_example_2(self):
        s, p = "abab", "ab"
        expected_output = [0, 1, 2]
        actual_output = self.solution.findAnagrams(s, p)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_3(self):
        s, p = "aa", "bb"
        expected_output = []
        actual_output = self.solution.findAnagrams(s, p)
        self.assertCountEqual(actual_output, expected_output)

    def test_single_character_string(self):
        s, p = "a", "a"
        expected_output = [0]
        actual_output = self.solution.findAnagrams(s, p)
        self.assertCountEqual(actual_output, expected_output)

    def test_no_anagram(self):
        s, p = "abc", "def"
        expected_output = []
        actual_output = self.solution.findAnagrams(s, p)
        self.assertCountEqual(actual_output, expected_output)

    def test_repeating_characters(self):
        s, p = "aabbbcc", "abc"
        expected_output = []
        actual_output = self.solution.findAnagrams(s, p)
        self.assertCountEqual(actual_output, expected_output)

    def test_large_input(self):
        s, p = "x" * 30000 + "y" + "z" * 15000 + "y" + "x" * 15000, "xyz"
        expected_output = [29999, 45000]
        actual_output = self.solution.findAnagrams(s, p)
        self.assertCountEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()
    