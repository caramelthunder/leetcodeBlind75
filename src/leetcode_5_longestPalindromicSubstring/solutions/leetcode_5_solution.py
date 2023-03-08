class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""

        get_len = lambda x: x[1] - x[0] + 1
        n = len(s)
        longest_palin_range = (0, 0)

        for i in range(n):
            
            odd_palin_range = self._longestPalindrome(s, i, i, n)
            if get_len(odd_palin_range) > get_len(longest_palin_range):
                longest_palin_range = odd_palin_range
            
            even_palin_range = self._longestPalindrome(s, i, i + 1, n)
            if get_len(even_palin_range) > get_len(longest_palin_range):
                longest_palin_range = even_palin_range

        L, R = longest_palin_range
        return s[L: R + 1]

    def _longestPalindrome(self, s, L, R, n):
        while (0 <= L and R < n) and s[L] == s[R]:
            L -= 1
            R += 1
        return (L + 1, R - 1)

