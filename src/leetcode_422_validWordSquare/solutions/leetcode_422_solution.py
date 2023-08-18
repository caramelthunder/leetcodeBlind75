from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        """
        Determines if a given list of words forms a valid word square.

        Args:
            words (List[str]): A list of words.

        Returns:
            bool: True if the words form a valid word square, False otherwise.

        Runtime and space complexity:
            Time(n): O(n^2) where n is the length of the longest word in the list.
            Space(n): O(1) as we're using a constant amount of space.
        """
        for row in range(len(words)):
            for col in range(len(words[row])):
                # Check whether position `[col][row]` is valid and if the characters match
                if (
                    not (col < len(words) and row < len(words[col]))
                    or words[row][col] != words[col][row]
                ):
                    return False
        return True
