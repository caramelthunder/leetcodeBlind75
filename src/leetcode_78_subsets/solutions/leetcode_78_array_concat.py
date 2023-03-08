class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []

        return self._subsets(nums, 0)

    def _subsets(self, nums, start):
        if start == len(nums):
            return [[]]
        
        val = nums[start]
        subsets_without_val = self._subsets(nums, start + 1)
        subsets_with_val = []

        for subset in subsets_without_val:
            subsets_with_val.append([val] + subset)

        return  subsets_with_val + subsets_without_val