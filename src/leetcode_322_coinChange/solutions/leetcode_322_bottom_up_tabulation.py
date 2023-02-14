from collections import deque

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf') for _ in range((amount))]
        
        for coin in coins:
            for amnt in range(coin, amount + 1):
                dp[amnt] = min(dp[amnt], dp[amnt - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
 
                



'''
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
'''