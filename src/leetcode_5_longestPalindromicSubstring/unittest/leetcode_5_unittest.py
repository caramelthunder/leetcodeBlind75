import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_5_solution import Solution as Solution1
from solutions.leetcode_5_solution_plus import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        s = "babad"
        expected_output = ["bab", "aba"]

        actual_output = self.solution1.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)

    def test_example_2(self):
        s = "cbbd"
        expected_output = ["bb"]

        actual_output = self.solution1.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)
    
    def test_example_3(self):
        s = "aacabdkacaa"
        expected_output = ["aca"]

        actual_output = self.solution1.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)
    
    def test_example_4(self):
        s = "a"
        expected_output = ["a"]

        actual_output = self.solution1.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)

        actual_output = self.solution2.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()