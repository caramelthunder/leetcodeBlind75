class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Given an array nums containing n distinct numbers in the range [0, n], 
        return the only number in the range that is missing from the array.

        Args:
            nums (list[int]): Array nums containing n distinct numbers.

        Returns:
            int: The only number in the range that is missing from the array.
        
        Runtime Analysis:
            Time complexity:    O(n), Take 2 * O(n) to calculate the sums.
            Space complexity:   O(1)
        """
        n = len(nums)
        expected_sum = sum(range(n + 1))
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum