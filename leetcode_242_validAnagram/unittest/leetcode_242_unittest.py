import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_242_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        params = (
            "anagram",
            "nagaram"
        )
        expected_output = True
        actual_output = self.solution.isAnagram(*params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example2(self):
        params = (
            "rat",
            "car"
        )
        expected_output = False
        actual_output = self.solution.isAnagram(*params)
        self.assertEqual(actual_output, expected_output)

    def test_example3(self):
        params = (
            "",
            ""
        )
        expected_output = True
        actual_output = self.solution.isAnagram(*params)
        self.assertEqual(actual_output, expected_output)

    def test_large_input(self):
        s = 'a' * (5 * 104)
        t = 'a' * (5 * 104)
        params = (s, t)
        expected_output = True
        actual_output = self.solution.isAnagram(*params)
        self.assertEqual(actual_output, expected_output)
        
    def test_special_characters(self):
        s = 'a b c'
        t = 'c b a'
        params = (s, t)
        expected_output = True
        actual_output = self.solution.isAnagram(*params)
        self.assertEqual(actual_output, expected_output)
        
    def test_unicode(self):
        s = 'a🙂b'
        t = 'b🙂a'
        params = (s, t)
        expected_output = True
        actual_output = self.solution.isAnagram(*params)
        self.assertEqual(actual_output, expected_output)
        
    def test_numbers_symbols(self):
        s = 'a1b#'
        t = '#b1a'
        params = (s, t)
        expected_output = True
        actual_output = self.solution.isAnagram(*params)
        self.assertEqual(actual_output, expected_output)

###############################
if __name__ == '__main__':
    unittest.main()