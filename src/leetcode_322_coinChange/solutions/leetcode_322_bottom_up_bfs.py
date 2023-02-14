from collections import deque

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        count = 0
        visited = set()

        q = deque([(amount, count)])
        visited.add(amount)
        while q:
            amount, count = q.popleft()
            if amount == 0:
                return count
            
            for coin in coins:
                new_amount = amount - coin
                if new_amount >= 0 and new_amount  not in visited:
                    visited.add(new_amount)
                    q.append((amount - coin, count + 1))

        return -1