class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        def binary_search(nums, target, end):
            left, right = 0, end
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        tails = [0] * len(nums)
        size = 0
        
        for num in nums:
            idx = binary_search(tails, num, size)
            tails[idx] = num
            size = max(size, idx + 1)
        
        return size