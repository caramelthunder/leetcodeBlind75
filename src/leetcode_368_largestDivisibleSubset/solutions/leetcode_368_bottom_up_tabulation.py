class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        nums.sort()
        lds = []
        dp = [([num]) for num in nums]

        for i, dividend in enumerate(nums):
            for j in range(i):
                divisor = nums[j]

                if dividend % divisor == 0:
                    if len(dp[j]) + 1 >= len(dp[i]):
                        dp[i] = dp[j] + [dividend]
            
            if len(dp[i]) >= len(lds):
                lds = dp[i][:]
    
        return lds