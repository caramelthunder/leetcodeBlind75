class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target: # target found.
                return mid
            
            # mid value belong to the left sorted half.
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # go left
                else:
                    left = mid + 1  # go right
                    
            else: # mid value belong to the right sorted half.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # go right
                else:
                    right = mid - 1 # go left
                    
        return -1
