class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)

        if n < 3:
            return False

        for one in range(len(nums)):
            for two in range(n - 1, one, -1):
                if nums[one] < nums[two] and two - one + 1 >= 3:
                    for three in range(two - 1, one, -1):
                        if nums[three] > nums[two]:
                            return True
            
        return False