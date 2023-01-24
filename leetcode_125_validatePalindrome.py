'''
https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not(s[left].isalnum()):
                left += 1
            while left < right and not(s[right].isalnum()):
                right  -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()

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
