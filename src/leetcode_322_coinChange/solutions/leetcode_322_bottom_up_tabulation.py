from collections import deque

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf') for _ in range((amount))]
        
        for coin in coins:
            for amnt in range(coin, amount + 1):
                dp[amnt] = min(dp[amnt], dp[amnt - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1