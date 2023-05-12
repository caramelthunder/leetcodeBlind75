class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Perform integer division without using the division or multiplication operations.

        Args:
            dividend (int): The number to be divided.
            divisor (int): The number to divide by.

        Returns:
            int: The result of the division operation.

        Time Complexity Analysis:
            This function runs in O(log N) time complexity, where N is the dividend.
            This is because we divide the problem space in half each time in the while loop.

        Space Complexity Analysis:
            The space complexity is O(1), as we use a constant amount of space to store variables.
            We do not use any data structures that grow with the input size.
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        if dividend == MIN_INT and divisor == (-1):
            return MAX_INT

        dividend_is_positive, divisor_is_positive = dividend >= 0, divisor >= 0
        is_negative = dividend_is_positive ^ divisor_is_positive

        # Convert both dividend and divisor to their negative equivalents to handle Python's rounding towards zero behavior.
        dividend = -dividend if dividend_is_positive else dividend
        divisor = -divisor if divisor_is_positive else divisor

        res = 0
        double = divisor
        pow_of_two = -1

        while double >= dividend:
            if double < MIN_INT // 2:
                break

            double += double
            pow_of_two += pow_of_two

        while dividend <= divisor:
            if double >= dividend:
                res += pow_of_two
                dividend -= double

            # Divide the double and power of two by 2
            double >>= 1
            pow_of_two >>= 1

        return res if is_negative else -res
