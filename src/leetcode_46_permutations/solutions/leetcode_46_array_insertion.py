class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [[nums[0]]]

        val = nums[0]
        perms_without_val = self.permute(nums[1:])
        ouput = []

        for perm in perms_without_val:
            for i in range(len(perm) + 1):
                prefix, suffix = perm[:i], perm[i:]
                ouput.append(prefix + [val] + suffix)
        
        return ouput
