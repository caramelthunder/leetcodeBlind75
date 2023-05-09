class Solution:

    def reverse(self, x: int) -> int:
        """
        Reverse the input integer while ensuring the output does not exceed the 32-bit signed integer range.

        Args:
            x (int): Input integer to reverse.

        Returns:
            int: Reversed integer. If the reversed integer would exceed the 32-bit signed integer range,
                 returns 0.

        Time Complexity Analysis:
            O(log10(n)): The while loop iterates through each digit of the input integer, and the number of
                         iterations is proportional to the number of digits (log10(n)) in the input integer.

        Space Complexity Analysis:
            O(1): The algorithm uses a constant amount of additional space to store variables, regardless
                  of the input size.
        """

        LIMIT = 2**31

        _positive = x>=0
        x = -x if not _positive else x
        res = 0

        while x > 0:
            x, remainder = divmod(x, 10)

            if not self._within_range(res, remainder, LIMIT, _positive):
                return 0
            res = res*10 + remainder

        return res if _positive else -res
    
    def _within_range(self, num, addition, LIMIT, _positive):
        allowance = LIMIT - num*10
        if _positive:
            return (num < LIMIT//10) or (num == LIMIT//10 and allowance > addition)
        else:
            return (num < LIMIT//10) or (num == LIMIT//10 and allowance >= addition)