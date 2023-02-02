class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        char_map = {}
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            
            if comp in char_map:
                return [char_map[comp], i]
            char_map[num] = i
            
        return [-1, -1]
