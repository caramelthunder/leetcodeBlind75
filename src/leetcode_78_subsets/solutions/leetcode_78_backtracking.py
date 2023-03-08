class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []

        output = []
        self._subsets(nums, 0, output, [])
        return output

    def _subsets(self, nums, i, output, subset= []):
        if i >= len(nums):
            output.append(subset[:])
            return
        
        # Include val in current subset.
        subset.append(nums[i])
        self._subsets(nums, i + 1, output, subset)
        subset.pop()
        
        # Exclude val in current subset.
        self._subsets(nums, i + 1, output, subset)
        