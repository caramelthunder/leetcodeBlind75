class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []
        self._permute(nums, 0, [], output)
        return output
    
    def _permute(self, nums, start, curr, output):
        if start >= len(nums):
            output.append(curr[:])
            return 
        
        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            curr.append(nums[start])
            
            self._permute(nums, start + 1, curr, output)

            curr.pop()
            nums[i], nums[start] = nums[start], nums[i]
