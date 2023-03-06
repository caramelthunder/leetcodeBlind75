class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        _sum = sum(nums)

        if _sum % 2 != 0:
            return False
            
        return self._canPartition(nums, 0, _sum // 2, {})
    
    def _canPartition(self, nums, i, amount, cache):
        if amount == 0:
            return True
        
        if amount < 0 or i >= len(nums):
            return False

        key = (i, amount)
        if key not in cache:

            for new_amount in [amount, amount - nums[i]]:
                attempt = self._canPartition(nums, i + 1, new_amount, cache)
                if attempt:
                    cache[key] = True
                    return True

            cache[key] = False
        return cache[key]