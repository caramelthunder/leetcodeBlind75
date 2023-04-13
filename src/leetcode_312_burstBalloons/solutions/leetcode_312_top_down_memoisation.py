class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # add virtual balloons at the start and end
        nums = [1] + nums + [1]
        # set left and right boundaries
        L, R = 1, len(nums) - 2
        # initialize cache.
        cache = {}
        # call the helper function with memoization
        return self._maxCoins(nums, L, R, cache)
    
    def _maxCoins(self, nums, L, R, cache):
        # base case: no balloon left, return zero coins
        if L > R:
            return 0

        key = (L, R)
        if key not in cache:
            # consider each balloon as the last to be bursted
            max_gain = 0
            for i in range(L, R + 1):
                gain_i = nums[L - 1] * nums[i] * nums[R + 1] # coins gained by bursting balloon i
                gain_leftOf_i = self._maxCoins(nums, L, i - 1, cache) # coins gained by bursting balloons left of i
                gain_rightOf_i = self._maxCoins(nums, i + 1, R, cache) # coins gained by bursting balloons right of i

                # update max gain by considering all possible combinations
                max_gain = max(max_gain, gain_leftOf_i + gain_i + gain_rightOf_i)
                
            cache[key] = max_gain

        return cache[key]

# Time complexity analysis:
# The helper function _maxCoins is called recursively for each balloon, 
# and at each level, we consider all possible balloons as the last to be bursted.
# However, memoization allows us to avoid redundant computations and reuse previous results.
# Therefore, each set of arguments is computed at most once, and the total number of recursive calls is O(n^2),
# where n is the number of balloons. For each call, we do constant amount of work, which includes three multiplications
# and two recursive calls or one cache lookup. Therefore, the time complexity is O(n^3) without memoization and
# O(n^2) with memoization.

# Space complexity analysis:
# The maximum depth of recursion is n, which means the maximum number of sets of arguments and local variables
# that exist at the same time is n. The size of each set of arguments and local variables is constant.
# In addition, we use a cache to store the results of previous computations, which has a maximum size of O(n^2).
# Therefore, the space complexity is O(n^2).
