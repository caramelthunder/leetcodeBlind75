class Solution:
    MODULO = (10**9) + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self._numRollsToTarget(n, k, target, {})
    
    def _numRollsToTarget(self, rolls_left, dice_nums, target,cache= {}):
        if rolls_left == 0:
            return int(target == 0)
        
        if rolls_left < 0 or target < 0:
            return 0

        key = (rolls_left, target)
        if key not in cache:

            ways_to_target = 0
            for num in range(1, dice_nums + 1):
                ways_to_remainder = self._numRollsToTarget(rolls_left - 1, dice_nums, target - num, cache)
                
                if self.MODULO - ways_to_target >= ways_to_remainder:
                    ways_to_target += ways_to_remainder
                else:
                    ways_to_target = ways_to_remainder - (self.MODULO - ways_to_target)

            cache[key] = ways_to_target
        
        return cache[key] 
