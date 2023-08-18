from typing import List


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        Determines if a string can be permuted to form a palindrome.

        The approach is to use a set to track characters. As we iterate through the string:
            - If a character is not in the set, it's added.
            - If a character is already in the set, it's removed.
        By the end, if the length of the set is 0 or 1, it means the string can be permuted to form a palindrome.

        Args:
        - s (str): Input string.

        Returns:
        - bool: True if the string can be permuted to form a palindrome, otherwise False.

        Runtime and space complexity:
            Time(n): O(n), where n is the length of the string.
            Space(n): O(k), where k is the number of distinct characters in the string.
        """

        char_set = set()

        for char in s:
            if char not in char_set:
                char_set.add(char)
            else:
                char_set.remove(char)

        return len(char_set) <= 1
