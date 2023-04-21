class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determines whether a positive integer `n` is a happy number.
        A number is happy if, after repeatedly replacing it with the sum of the squares of its digits,
        the result becomes 1. If the result never becomes 1, the number is not a happy number.

        Args:
            n (int): The positive integer to check for happiness.

        Returns:
            bool: True if the number is happy, False otherwise.

        Time Complexity:
            The algorithm has a time complexity of O(log n) in the worst case, where n is the input integer. 
            This is because each iteration of `_isHappy` replaces `n` with the sum of the squares of its digits 
            in O(log n) time, and the `isHappy` function repeatedly calls `_isHappy` on `n` and its square-sum 
            until it either finds a cycle or reaches 1.

        Space Complexity:
            The algorithm has a space complexity of O(1), since it only uses a constant amount of extra space.

        """
        slow = n
        fast = self._isHappy(n)

        while fast != 1:
            if fast == slow:
                return False
            
            slow = self._isHappy(slow)
            fast = self._isHappy(self._isHappy(fast))
        return True

    def _isHappy(self, n):
        """
        Helper function that returns the sum of the squares of the digits of `n`.
        """
        next_n = 0
        while n > 0:
            n, remainder = divmod(n, 10)   # Get the next digit
            next_n += remainder ** 2       # Add the square of the digit to `next_n`
        return next_n
