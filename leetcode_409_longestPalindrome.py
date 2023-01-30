'''
https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

class Solution:
    def longestPalindrome(self, s: str): 
        char_map = {}
        pairs = 0

        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
            
            if char_map[char] == 2:
                pairs += 1
                del char_map[char]

        return pairs * 2 + int(len(char_map) > 0)

import unittest
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

##################################
if __name__ == '__main__':
    unittest.main()
