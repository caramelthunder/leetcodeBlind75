
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1 for _ in range(len(nums))]
        
        # Calculate the prefix products
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        # Calculate the suffix products and multiply them with the prefix products
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res