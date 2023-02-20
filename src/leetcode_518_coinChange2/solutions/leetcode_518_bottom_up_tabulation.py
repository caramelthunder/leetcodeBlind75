class Solution:
    def change(self, coins: list[int], amount: int) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        
        for i, coin in enumerate(coins, start= 1):
            for amnt in range(amount + 1):
                dp[i][amnt] = dp[i - 1][amnt] 
                if amnt >= coin:
                    dp[i][amnt] += dp[i][amnt - coin]
                    
        return dp[-1][-1] 
