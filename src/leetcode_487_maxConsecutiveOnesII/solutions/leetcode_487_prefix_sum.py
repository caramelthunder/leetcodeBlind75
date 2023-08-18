from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Determine the maximum number of consecutive 1's that can be achieved
        in the array by flipping at most one 0 to 1.

        This approach uses a prefix sum strategy to keep track of the number
        of consecutive 1's encountered so far. It resets the count of ones if two
        zeros are encountered without a one in between them.

        Args:
        - nums (List[int]): A binary list of size 1 <= len(nums) <= 10^5,
                            where each element is either 0 or 1.

        Returns:
        - int: The maximum number of consecutive 1's after flipping at most one 0.

        Runtime and space complexity:
        - Time(n): O(n). The solution iterates through the list once, which results
                   in a linear runtime complexity.
        - Space(n): O(1). Constant space is used irrespective of the size of the input list,
                   although the original list is modified.
        """

        max_ones = 0
        zero_idx = None
        ones_cnt = 0  # Count of 1's encountered so far.

        for i, num in enumerate(nums):
            ones_cnt += num

            if num == 0:
                if zero_idx is not None:
                    ones_cnt -= nums[zero_idx]
                zero_idx = i

            nums[i] = ones_cnt
            max_ones = max(max_ones, ones_cnt)

        # If a zero was encountered, consider its flip for additional consecutive 1.
        return max_ones + 1 if zero_idx is not None else max_ones
