class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        cache = {}
        seen = set()

        for i, val1 in enumerate(nums):
            if val1 not in seen:
                seen.add(val1)

                for j in range(i + 1, len(nums)):
                    val2 = nums[j]
                    comp = 0 - val1 - val2
                    if comp in cache and cache[comp] == i:
                        res.add(tuple(sorted([val1, val2, comp])))
                    cache[val2] = i
                
        return [list(triplet) for triplet in res]

'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''