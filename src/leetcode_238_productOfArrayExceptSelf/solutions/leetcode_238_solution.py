
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
            prefix = [1 for _ in range(len(nums))]
            for i in range(1, len(prefix)):
                prefix[i] = prefix[i - 1] * nums[i - 1]
            
            suffix = [1 for _ in range(len(nums))]
            for i in range (len(suffix) - 2, -1, -1):
                suffix[i] =  suffix[i + 1] * nums[i + 1]

            return [prefix[i] * suffix[i] for i in range(len(nums))]