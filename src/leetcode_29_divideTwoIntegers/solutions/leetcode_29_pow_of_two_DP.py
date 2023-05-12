class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Perform integer division without using multiplication, division, or mod operators.

        Args:
            dividend (int): The number to be divided.
            divisor (int): The number to divide by.

        Returns:
            int: The result of the division operation. If the result would overflow, return MAX_INT.

        Time Complexity Analysis:
            The time complexity is O(log(n)), where n is the absolute value of the dividend.
            This is because the algorithm uses binary search, repeatedly halving the dividend
            until it is less than the divisor.

        Space Complexity Analysis:
            The space complexity is O(log(n)) due to the storage of the power-of-two multiples
            of the divisor in the 'doubles_pow_of_two' list. The length of this list is proportional
            to the number of bits needed to represent the dividend, hence the log(n) space complexity.
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        # Handle overflow case
        if dividend == MIN_INT and divisor == (-1):
            return MAX_INT

        dividend_is_positive, divisor_is_positive = dividend >= 0, divisor >= 0
        is_negative = dividend_is_positive ^ divisor_is_positive

        # Convert both dividend and divisor to their negative equivalents,
        # this is to handle Python's rounding towards zero behavior during division
        dividend = -dividend if dividend_is_positive else dividend
        divisor = -divisor if divisor_is_positive else divisor

        res = 0
        doubles_pow_of_two = []
        double = divisor
        pow_of_two = -1

        while double >= dividend:
            doubles_pow_of_two.append((double, pow_of_two))

            if double < MIN_INT // 2:
                break

            double += double
            pow_of_two += pow_of_two

        while doubles_pow_of_two:
            double, pow_of_two = doubles_pow_of_two.pop()

            if double >= dividend:
                res += pow_of_two
                dividend -= double

            if dividend > divisor:
                break

        return res if is_negative else -res
