
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        cache = {}
        min_count = self._coinChange(coins, amount, cache)
        return min_count if min_count != float('inf') else -1

    def _coinChange(self, coins, amount, cache):
        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')

        if amount not in cache:
            
            min_count = float('inf')
            for coin in coins:
                count = self._coinChange(coins, amount - coin, cache)
                min_count = min(min_count, count + 1)
            cache[amount] = min_count

        return cache[amount]
                



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