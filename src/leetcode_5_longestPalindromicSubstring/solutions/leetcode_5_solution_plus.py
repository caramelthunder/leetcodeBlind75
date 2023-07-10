class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palin_len = 0
        max_palin_range = (0, 0)

        for i in range(n := len(s)):
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1  # expand to cover repeated chars

            # even length
            if j != i:
                start, end = self._center_expansion(s, i, j)
                if (palin_len := self._get_distance(start, end)) > max_palin_len:
                    max_palin_len = palin_len
                    max_palin_range = (start, end)
                i = j  # skip over repeated char
                
            else:  # odd length
                start, end = self._center_expansion(s, i, j)
                if (palin_len := self._get_distance(start, end)) > max_palin_len:
                    max_palin_len = palin_len
                    max_palin_range = (start, end)
           
        return s[max_palin_range[0]: max_palin_range[1] + 1]

    def _get_distance(self, start, end) -> int:
        return end - start + 1
    
    def _center_expansion(self, s, left, right) -> tuple[int, int]:
        while 0 <= left <= right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (left + 1, right - 1)