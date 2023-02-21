
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        self._combinationSum(candidates, 0, target, [], output)
        return output
    
    def _combinationSum(self, nums, idx, target, curr, output):
        if target == 0:
            output.append(curr[:])
            return
        
        if target < 0:
            return 
        
        for i in range(idx, len(nums)):
            num = nums[i]

            curr.append(num)

            remain = target - num
            self._combinationSum(nums, i, remain, curr, output)

            curr.pop()