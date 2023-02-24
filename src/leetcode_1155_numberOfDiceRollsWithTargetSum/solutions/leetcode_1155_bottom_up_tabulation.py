class Solution:
    MODULO = (10**9) + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        prev = [0 for _ in range(target + 1)]
        for amount in range(1, target + 1):
           prev[amount] = int(k >= amount)

        curr = prev[:]

        roll_left = n - 1
        while roll_left > 0:

            for amount in range(1, target + 1):
                curr[amount] = 0
                for i in range(1, min(k, amount) + 1):
                    if (self.MODULO - curr[amount]) < prev[amount - i]:
                        curr[amount] = prev[amount - i] - (self.MODULO - curr[amount]) 
                    else:
                        curr[amount] = (curr[amount] + prev[amount - i])  % self.MODULO

            prev = curr[:]
            roll_left -= 1

        return curr[target]