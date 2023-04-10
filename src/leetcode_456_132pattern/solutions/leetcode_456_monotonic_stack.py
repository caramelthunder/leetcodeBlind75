class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        """
        Finds if there exists a 132 pattern in the given array.

        Args:
            nums: List of integers.
        Returns:
            True if there exists a 132 pattern, False otherwise.

        Time complexity:
        O(n) - The function loops through the input array twice, 
        and each element is pushed and popped from the stack at most once.

        Space complexity:
        O(n) - The function uses an array of size n to store the minimum prefix array, 
        and a stack to store the possible third elements of the 132 pattern.
        """
        n = len(nums)

        # Handle invalid input.
        if n < 3:
            return False

        # Compute the minimum prefix array
        prefix_min = [nums[0]]
        for num in nums[1:]:
            prefix_min.append(min(prefix_min[-1], num))

        # Traverse the array from right to left
        stack = []
        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):

            if nums[i] > prefix_min[i]:
                # Find the possible second (mid_val) and third (max_val) elements of the 132 pattern
                max_num = nums[i]
                min_num = prefix_min[i]

                # Pop elements from the stack that are less than or equal to the minimum value
                # They cannot be the third element in the 132 pattern
                while stack and stack[-1] <= min_num:
                    stack.pop()

                # If there is an element in the stack that is less than or equal to the maximum value
                # We have found a 132 pattern
                if stack and stack[-1] < max_num:
                    return True
                
                # Push the maximum value onto the stack as a candidate for the third element
                stack.append(max_num)

        # No 132 pattern found
        return False