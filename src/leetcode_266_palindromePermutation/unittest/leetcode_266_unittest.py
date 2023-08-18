import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_266_solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.canPermutePalindrome("aab"))

    def test_example_2(self):
        self.assertFalse(self.solution.canPermutePalindrome("code"))

    def test_example_3(self):
        self.assertTrue(self.solution.canPermutePalindrome("carerac"))

    def test_palindrome(self):
        self.assertTrue(self.solution.canPermutePalindrome("radar"))

    def test_rearrange_to_palindrome(self):
        self.assertTrue(self.solution.canPermutePalindrome("aarr"))

    def test_not_palindrome(self):
        self.assertFalse(self.solution.canPermutePalindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(self.solution.canPermutePalindrome(""))

    def test_single_char_string(self):
        self.assertTrue(self.solution.canPermutePalindrome("a"))

    def test_even_characters_not_palindrome(self):
        self.assertFalse(self.solution.canPermutePalindrome("abcd"))

    def test_odd_characters_not_palindrome(self):
        self.assertFalse(self.solution.canPermutePalindrome("abcde"))

    def test_odd_characters_palindrome(self):
        self.assertTrue(self.solution.canPermutePalindrome("aabbccddz"))


######################################
if __name__ == "__main__":
    unittest.main()
