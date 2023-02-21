
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        self._combinationSum(candidates, 0, target, [], output)
        return output
    
    def _combinationSum(self, nums, idx, target, curr, output):
        if target == 0:
            output.append(curr[:])
            return
        
        if idx >= len(nums) or target < 0:
            return 
        
        num = nums[idx]
        max_num_allowed = target // num

        for cnt in range(max_num_allowed + 1):
            for _ in range(cnt):
                curr.append(num)

            remain = target - num * cnt
            self._combinationSum(nums, idx + 1, remain, curr, output)

            for _ in range(cnt):
                curr.pop()