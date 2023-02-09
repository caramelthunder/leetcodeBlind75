class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        seen = set()
        res = []

        def twoSum(i):
            L, R = i + 1, len(nums) - 1
            while L < R:
                _sum = nums[i] + nums[L] + nums[R]
                if _sum < 0:
                    L += 1
                elif _sum > 0:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    
        for i, num in enumerate(nums):
            if num <= 0 and nums[i] not in seen:
                seen.add(num)
                twoSum(i)
        return res
    

'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''