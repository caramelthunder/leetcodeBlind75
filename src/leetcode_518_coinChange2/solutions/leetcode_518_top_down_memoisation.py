class Solution:
    def change(self, coins: list[int], amount: int) -> int:
        cache = {}
        return self._change(coins, 0, amount, cache)

    def _change(self, coins, idx, amount, cache):
        if amount == 0:
            return 1
        
        if idx >= len(coins):
            return 0

        key = (amount, idx)
        if key not in cache:

            coin = coins[idx]
            allowance = amount // coin

            count = 0
            for num_of_coins in range(allowance + 1):
                new_amount = amount - (coin * num_of_coins)
                count += self._change(coins, idx + 1, new_amount, cache)
            cache[key] = count
        
        return cache[key]