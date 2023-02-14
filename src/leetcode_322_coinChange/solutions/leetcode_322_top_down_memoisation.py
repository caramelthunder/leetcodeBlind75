
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