class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        nums.sort()
        cache = {}
        self._helper(nums, len(nums) - 1, cache)
        return max(cache.values(), key= len)

    def _helper(self, nums, i, cache):
            dividend = nums[i]

            if i == 0:
                cache[dividend] = ([nums[0]])
                return cache[dividend]

            if dividend not in cache:

                cache[dividend] = [dividend]
                for j in range(i - 1, -1, -1):
                    divisor = nums[j]
                    lds_divisor = self._helper(nums, j,cache)

                    if dividend % divisor == 0:
                        if len(lds_divisor) + 1 > len(cache[dividend]):
                            cache[dividend] = lds_divisor + [dividend]

            return cache[dividend]