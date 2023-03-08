import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_5_solution import Solution 

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        s = "babad"
        expected_output = ["bab", "aba"]

        actual_output = self.solution.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)

    def test_example_2(self):
        s = "cbbd"
        expected_output = ["bb"]

        actual_output = self.solution.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)
    
    def test_example_3(self):
        s = "aacabdkacaa"
        expected_output = ["aca"]

        actual_output = self.solution.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)
    
    def test_example_4(self):
        s = "a"
        expected_output = ["a"]

        actual_output = self.solution.longestPalindrome(s)
        self.assertIn(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()