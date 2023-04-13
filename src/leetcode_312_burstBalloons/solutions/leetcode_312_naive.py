class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # add virtual balloons at the start and end
        nums = [1] + nums + [1]
        # set left and right boundaries
        L, R = 1, len(nums) - 2
        # call the helper function
        return self._maxCoins(nums, L, R)
    
    def _maxCoins(self, nums, L, R):
        # base case: only one balloon left, return its coins
        if L == R:
            return nums[L - 1] * nums[L] * nums[L + 1]
        # base case: no balloon left, return zero coins
        if L > R:
            return 0

        max_gain = 0
        # consider each balloon as the last to be bursted
        for i in range(L, R + 1):
            gain_i = nums[L - 1] * nums[i] * nums[R + 1] # coins gained by bursting balloon i
            gain_leftOf_i = self._maxCoins(nums, L, i - 1) # coins gained by bursting balloons left of i
            gain_rightOf_i = self._maxCoins(nums, i + 1, R) # coins gained by bursting balloons right of i

            # update max gain by considering all possible combinations
            max_gain = max(max_gain, gain_leftOf_i + gain_i + gain_rightOf_i)
        
        return max_gain

# Time complexity analysis:
# The helper function _maxCoins is called recursively for each balloon, 
# and at each level, we consider all possible balloons as the last to be bursted.
# Therefore, the total number of recursive calls is n*(n+1)/2, where n is the number of balloons.
# For each call, we do constant amount of work, which includes three multiplications and two recursive calls.
# Therefore, the time complexity is O(n^3).

# Space complexity analysis:
# At each level of recursion, we create a new set of arguments and a new set of local variables.
# The maximum depth of recursion is n, which means the maximum number of sets of arguments and local variables
# that exist at the same time is n. The size of each set of arguments and local variables is constant.
# Therefore, the space complexity is O(n).
