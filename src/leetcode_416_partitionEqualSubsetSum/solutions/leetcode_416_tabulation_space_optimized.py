class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        
        target = _sum // 2
        dp = [True] + [False for _ in range(target)]

        for num in nums:
            for amount in range(target, num - 1, -1):
                dp[amount] = dp[amount] or dp[amount - num]
            
            if dp[target]:
                return True

        return False
