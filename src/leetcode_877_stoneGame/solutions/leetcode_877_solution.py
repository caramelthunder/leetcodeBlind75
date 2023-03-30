class Solution:
    def stoneGame(self, piles: list[int]) -> int:
        L, R = 0, len(piles) - 1

        prefix_sums = [0 for _ in range(len(piles) + 1)]
        for i in range(1, len(prefix_sums)):
            prefix_sums[i] = prefix_sums[i - 1] + piles[i - 1]
        
        Alice_max_score = self._stoneGame(prefix_sums, L, R, {})
        return Alice_max_score > (prefix_sums[-1] // 2)
    
    def _stoneGame(self, prefix_sums, L, R, cache):
        total_score = prefix_sums[R + 1] - prefix_sums[L]

        if L == R:
            return total_score
        
        key = (L, R)
        if key not in cache:
            _pick_left = self._stoneGame(prefix_sums, L + 1, R, cache)
            _pick_right = self._stoneGame(prefix_sums, L, R - 1, cache)

            _max_score = total_score - min(_pick_left, _pick_right)
            cache[key] = _max_score
            
        return cache[key]