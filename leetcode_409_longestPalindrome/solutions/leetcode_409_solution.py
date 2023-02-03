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