'''
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        magazine_map = Counter(magazine)

        for char in ransomNote:
            if magazine_map[char] == 0:
                return False
            magazine_map[char] -= 1

        return True

import unittest
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