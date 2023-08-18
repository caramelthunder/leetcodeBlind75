from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Determine the maximum number of consecutive 1's that can be achieved
        in the array by flipping at most one 0 to 1.

        Args:
        - nums (List[int]): A binary list of size 1 <= len(nums) <= 10^5,
                            where each element is either 0 or 1.

        Returns:
        - int: The maximum number of consecutive 1's after flipping at most one 0.

        Runtime and space complexity:
        - Time(n): O(n). The solution iterates through the list once with the right pointer and moves the left
                   pointer only when necessary, which results in a linear runtime complexity.
        - Space(n): O(1). Constant space is used irrespective of the size of the input list.
        """

        max_ones = 0  # Keeps track of the maximum number of consecutive 1's found so far.
        zeros_cnt = 0  # Count the number of zeros within the current window.
        left = 0  # Left boundary of the sliding window.

        for right, num in enumerate(nums):
            if num == 0:
                zeros_cnt += 1

            # Shift the left boundary of the window to the right when there are more than one 0's within it.
            while zeros_cnt > 1:
                if nums[left] == 0:
                    zeros_cnt -= 1
                left += 1

            # Update max_ones with the maximum of the previous value or the width of the current window.
            max_ones = max(max_ones, right - left + 1)

        return max_ones
