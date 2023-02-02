import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_125_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution()

    def test_example1(self):
        params = 'A man, a plan, a canal: Panama'
        expected_output = True
        actual_output = self.solution1.isPalindrome(params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example2(self):
        params = 'race a car'
        expected_output = False
        actual_output = self.solution1.isPalindrome(params)
        self.assertEqual(actual_output, expected_output)

    def test_example3(self):
        params = ' '
        expected_output = True
        actual_output = self.solution1.isPalindrome(params)
        self.assertEqual(actual_output, expected_output)

    def test_non_ASCII_chars(self):
        params = '¿cómo estás?'
        expected_output = False
        actual_output = self.solution1.isPalindrome(params)
        self.assertEqual(actual_output, expected_output)

#########################
if __name__ == '__main__':
    unittest.main()
