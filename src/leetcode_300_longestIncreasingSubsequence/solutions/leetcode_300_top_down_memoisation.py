class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        self.LIS_len = 1
        cache = {}
        self._lengthOfLIS(nums, len(nums) - 1, cache)
        return self.LIS_len

    def _lengthOfLIS(self, nums, i, cache):
        if i == 0:
            return 1
        
        if i not in cache:

            candidate = 0
            for j in range(i - 1, -1, -1):
                LIS_len_j = self._lengthOfLIS(nums, j, cache)
                if nums[j] < nums[i]:
                    candidate = max(candidate, LIS_len_j)
                    
            self.LIS_len = max(self.LIS_len, candidate + 1)
            cache[i] = candidate + 1

        return cache[i]

