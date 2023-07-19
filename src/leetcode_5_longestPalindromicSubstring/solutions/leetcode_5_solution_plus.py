class Solution:
    def longestPalindrome(self, s: str) -> str:

        def _get_distance(start, end) -> int:
            return end - start + 1

        def _center_expansion(left, right) -> tuple[int, int]:
            while 0 <= left <= right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right - 1)

        max_palin_len = 0
        max_palin_range = (0, 0)

        i = 0
        while i < (n := len(s)):
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1  # expand to cover repeated chars

            start, end = _center_expansion(i, j)
            if (palin_len := _get_distance(start, end)) > max_palin_len:
                max_palin_len = palin_len
                max_palin_range = (start, end)

            i = j + 1

        return s[max_palin_range[0]: max_palin_range[1] + 1]