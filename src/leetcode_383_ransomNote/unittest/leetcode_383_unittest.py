import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_383_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        ransomNote = "aa"
        magazine = "ab"
        expected_output = False
        actual_output = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        ransomNote = "a"
        magazine = "b"
        expected_output = False
        actual_output = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        ransomNote = "aa"
        magazine = "aab"
        expected_output = True
        actual_output = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(actual_output, expected_output)
    
    def test_empty_ransomNote(self):
        ransomNote = ""
        magazine = "abcdefghijklmnopqrstuvwxyz"
        expected_output = True
        actual_output = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(actual_output, expected_output)

    def test_empty_magazine(self):
        ransomNote = "abcdefghijklmnopqrstuvwxyz"
        magazine = ""
        expected_output = False
        actual_output = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(actual_output, expected_output)
    
    def test_special_characters(self):
        ransomNote = "abc123"
        magazine = "abcdefghijklmnopqrstuvwxyz1234567890"
        expected_output = True
        actual_output = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(actual_output, expected_output)

    def test_magazine_shorter_ransomNote(self):
        ransomNote = "abcdefghijkkk"
        magazine = "abcdefghijkk"
        expected_output = False
        actual_output = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(actual_output, expected_output)

    def test_larger_inputs(self):
        ransomNote = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};':\"\\|,.<>/?`~"*1000
        magazine = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};':\"\\|,.<>/?`~"*1000
        expected_output = True
        actual_output = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(actual_output, expected_output)

##############################
if __name__ == '__main__':
    unittest.main()