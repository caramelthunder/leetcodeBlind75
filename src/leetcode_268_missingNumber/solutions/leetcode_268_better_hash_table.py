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
            Time complexity:    O(n), Take O(n) to add num to set + O(n) to iterate from 0 to n.
            Space complexity:   O(n) to store the set of nums.
        """

        n = len(nums)
        actual_nums = set(nums)

        for expected_num in range(n + 1):
            if expected_num not in actual_nums:
                return expected_num