class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_over = 0
        ans = ''

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            _sum = x + y + carry_over
            ans = str(_sum % 2) + ans
            carry_over = _sum // 2

            i -= 1
            j -= 1

        return '1' + ans if carry_over else ans