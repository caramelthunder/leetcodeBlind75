class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        dp = [1 for _ in range(len(nums))]
        LIS_len = 1

        for R in range(1, len(nums)):
            for L in range(R):
                if nums[L] < nums[R]:
                    dp[R] = max(dp[R], dp[L] + 1)
            LIS_len = max(LIS_len, dp[R])

        return LIS_len