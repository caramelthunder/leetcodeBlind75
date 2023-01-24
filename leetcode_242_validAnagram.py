'''
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = Counter(s)
        
        for char in t:
            if char in s_chars:
                s_chars[char] -= 1
                if s_chars[char] == 0:
                    del s_chars[char]
            else:
                return False

        return len(s_chars) == 0

import unittest
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