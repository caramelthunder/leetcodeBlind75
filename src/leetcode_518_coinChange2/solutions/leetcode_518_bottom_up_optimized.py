class Solution:
    def change(self, coins: list[int], amount: int) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for amnt in range(coin, amount + 1):
                dp[amnt] += dp[amnt - coin]
                
        return dp[-1]