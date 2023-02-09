import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_409_solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "abccccdd"
        expected_output = 7
        actual_output = self.solution.longestPalindrome(s)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        s = "a"
        expected_output = 1
        actual_output = self.solution.longestPalindrome(s)
        self.assertEqual(actual_output, expected_output)

    def test_mixed_cases(self):
        s = "aAaaA"
        expected_output = 5
        actual_output = self.solution.longestPalindrome(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_empty_string(self):
        s = ""
        expected_output = 0
        actual_output = self.solution.longestPalindrome(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_even_length_only_even_frequency(self):
        s = "aabbccdd"
        expected_output = 8
        actual_output = self.solution.longestPalindrome(s)
        self.assertEqual(actual_output, expected_output)

    def test_odd_length_only_odd_frequency(self):
        s = "abcddcbaa"
        expected_output = 9
        actual_output = self.solution.longestPalindrome(s)
        self.assertEqual(actual_output, expected_output)

    def test_odd_length_mixed_frequency(self):
        s = "aabccddc"
        expected_output = 7
        actual_output = self.solution.longestPalindrome(s)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_longest_palindrome(self):
        s = "aabbccddeeffgghh"
        expected_output = 16
        actual_output = self.solution.longestPalindrome(s)
        self.assertEqual(actual_output, expected_output)

##################################
if __name__ == '__main__':
    unittest.main()
