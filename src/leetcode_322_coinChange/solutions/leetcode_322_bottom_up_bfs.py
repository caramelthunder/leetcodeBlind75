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