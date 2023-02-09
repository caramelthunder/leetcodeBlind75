import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_3_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        s = "abcabcbb"
        expected_output = 3
        actual_output = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        s = "bbbbb"
        expected_output = 1
        actual_output = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        s = "pwwkew"
        expected_output = 3
        actual_output = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual_output, expected_output)
    
    def test_empty_string(self):
        s = ""
        expected_output = 0
        actual_output = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual_output, expected_output)
        
    def test_single_char_string(self):
        s = "a"
        expected_output = 1
        actual_output = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual_output, expected_output)

    def test_alternating_char_string(self):
        s = "ababab"
        expected_output = 2
        actual_output = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual_output, expected_output)

#########################
if  __name__ == '__main__':
    unittest.main()