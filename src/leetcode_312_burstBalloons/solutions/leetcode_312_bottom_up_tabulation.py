class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # add virtual balloons at the start and end
        nums = [1] + nums + [1]
        # set left and right boundaries
        L, R = 1, len(nums) - 2
        # initialize cache with base cases
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # fill in the dp table bottom-up
        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                # consider each balloon as the last to be bursted
                for i in range(left, right + 1):
                    gain_i = nums[left - 1] * nums[i] * nums[right + 1] # coins gained by bursting balloon i
                    gain_leftOf_i = dp[left][i - 1] # coins gained by bursting balloons left of i
                    gain_rightOf_i = dp[i + 1][right] # coins gained by bursting balloons right of i

                    # update dp table by considering all possible combinations
                    dp[left][right] = max(dp[left][right], gain_leftOf_i + gain_i + gain_rightOf_i)

        # return the result
        return dp[L][R]

# Time complexity analysis:
# The dp table has n^2 entries, and each entry requires O(n) computations,
# because we need to consider all possible balloons between left and right as the last to be bursted.
# Therefore, the total number of computations is O(n^3), where n is the number of balloons.
# However, dynamic programming allows us to avoid redundant computations and reuse previous results.
# Therefore, the actual number of computations is much smaller, and the time complexity is O(n^3).

# Space complexity analysis:
# The dp table has n^2 entries, each of which requires O(1) space. Therefore, the space complexity is O(n^2).
