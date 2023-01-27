'''
https://leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation:    There are two ways to climb to the top.
                1. 1 step + 1 step
                2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation:    There are three ways to climb to the top.
                1. 1 step + 1 step + 1 step
                2. 1 step + 2 steps
                3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45
'''

class Solution_Top_Down:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self._climbStairs(n, cache)
    
    def _climbStairs(self, n, cache):
        if n == 0 or n == 1:
            return 1

        if n not in cache:
            cache[n] = self._climbStairs(n - 1, cache) + self._climbStairs(n - 2, cache) 
        return cache[n]

class Solution_Bottom_Up:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

class Solution_Bottom_Up_Constant_Space:
    def climbStairs(self, n: int) -> int:
        from_one = 1
        from_two = 1

        for _ in range(2, n + 1):
            curr = from_one + from_two
            from_two = from_one
            from_one = curr

        return curr

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.solution_top_down = Solution_Top_Down()
        self.solution_bottom_up = Solution_Bottom_Up()
        self.solution_bottom_up_constant_space = Solution_Bottom_Up_Constant_Space()
    
    def test_example_1(self):
        n = 2
        expected_output = 2

        actual_output_top_down = self.solution_top_down.climbStairs(n)
        self.assertEqual(actual_output_top_down, expected_output)

        actual_output_bottom_up = self.solution_bottom_up.climbStairs(n)
        self.assertEqual(actual_output_bottom_up, expected_output)

        actual_output_bottom_up_constant_space = self.solution_bottom_up_constant_space.climbStairs(n)
        self.assertEqual(actual_output_bottom_up_constant_space, expected_output)

    def test_example_2(self):
        n = 3
        expected_output = 3

        actual_output_top_down = self.solution_top_down.climbStairs(n)
        self.assertEqual(actual_output_top_down, expected_output)

        actual_output_bottom_up = self.solution_bottom_up.climbStairs(n)
        self.assertEqual(actual_output_bottom_up, expected_output)

        actual_output_bottom_up_constant_space = self.solution_bottom_up_constant_space.climbStairs(n)
        self.assertEqual(actual_output_bottom_up_constant_space, expected_output)

    def test_example_3(self):
        n = 5
        expected_output = 8

        actual_output_top_down = self.solution_top_down.climbStairs(n)
        self.assertEqual(actual_output_top_down, expected_output)

        actual_output_bottom_up = self.solution_bottom_up.climbStairs(n)
        self.assertEqual(actual_output_bottom_up, expected_output)

        actual_output_bottom_up_constant_space = self.solution_bottom_up_constant_space.climbStairs(n)
        self.assertEqual(actual_output_bottom_up_constant_space, expected_output)

    def test_example_4(self):
        n = 6
        expected_output = 13

        actual_output_top_down = self.solution_top_down.climbStairs(n)
        self.assertEqual(actual_output_top_down, expected_output)

        actual_output_bottom_up = self.solution_bottom_up.climbStairs(n)
        self.assertEqual(actual_output_bottom_up, expected_output)

        actual_output_bottom_up_constant_space = self.solution_bottom_up_constant_space.climbStairs(n)
        self.assertEqual(actual_output_bottom_up_constant_space, expected_output)

#########################
if __name__ == '__main__':
    unittest.main()