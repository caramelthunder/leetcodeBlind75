class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum