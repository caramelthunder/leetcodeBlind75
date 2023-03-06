class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        
        nums = [0] + nums
        target = _sum // 2
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        dp[0][0] = True

        for i in range(1, len(nums)):
            num = nums[i]

            for amount in range(target + 1):
                if amount >= num:
                    dp[i][amount] = dp[i - 1][amount] or dp[i - 1][amount - num]
                else:
                    dp[i][amount] = dp[i - 1][amount]

            if dp[i][target]:
                return True

        return False
