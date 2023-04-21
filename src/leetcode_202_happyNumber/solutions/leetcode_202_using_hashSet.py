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
            The algorithm has a time complexity of O(log^2 n) in the worst case, 
            where n is the input integer. This is because the number of digits in `n` is O(log n), 
            and each iteration of the inner while loop takes O(log n) time.

        Space Complexity:
            The algorithm has a space complexity of O(log n) in the worst case, 
            where n is the input integer. This is because the size of the `seen` set 
            is proportional to the number of distinct numbers seen during the algorithm's execution.

        """
        seen = set()    # Set to store previously seen numbers

        while n != 1:
            # If we've seen the number before, it's in a cycle and can't be happy
            if n in seen:
                return False

            seen.add(n)     # Add the number to the set of seen numbers
            next_n = 0      # Calculate the next number

            # Replace `n` with the sum of the squares of its digits
            while n > 0:
                n, remainder = divmod(n, 10)    # Get the next digit
                next_n += remainder ** 2        # Add the square of the digit to `next_n`
            
            n = next_n      # Set `n` to the next number

        return True     # If we reach 1, the number is happy

