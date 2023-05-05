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
            Time complexity:    O(nlogn), Take O(nlogn) to sort the array + O(n) to iterate the array.
                                overall O(nlogn).                   
            Space complexity:   O(n) to store the sorted array, O(1) if sort the array in-place.
        """

        n = len(nums)
        sorted_nums = sorted(nums)

        # First num, 0 is missing.
        if sorted_nums[0] != 0:
            return 0

        for i in range(len(sorted_nums) - 1):
            _curr, _next = sorted_nums[i], sorted_nums[i + 1]
            if _curr + 1 != _next:
                return _curr + 1

        # Last num, n is missing.
        return n