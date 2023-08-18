class Solution:
    def confusingNumber(self, n: int) -> bool:
        """Determine if a given number is a confusing number.

        A confusing number is a number that, when rotated 180 degrees,
        becomes a different number with each of its digits still valid.

        Args:
            n (int): The input number to check.

        Returns:
            bool: True if n is a confusing number, otherwise False.

        Runtime and space complexity:
            Time(n): O(log n), where n is the given number.
                     We're iterating through each digit of the number.
            Space(n): O(1), as the space used by the 'rotatables' dictionary
                      and other variables is constant irrespective of the input.

        Examples:
            confusingNumber(6)  -> True,  because 6 becomes 9 when rotated.
            confusingNumber(89) -> True,  because 89 becomes 98 when rotated.
            confusingNumber(11) -> False, because 11 remains 11 when rotated.
        """

        rotatables = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        num = n
        rotated_num = 0

        while num > 0:
            remainder = num % 10
            if remainder not in rotatables:
                return False
            rotated_num = rotated_num * 10 + rotatables[remainder]
            num = num // 10

        return rotated_num != n
