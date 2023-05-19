from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given a list of non-negative integers representing the heights of vertical walls,
        this function calculates how much rainwater can be trapped between the walls.

        This implementation uses two pointers, L and R, traversing the array from the left and right, respectively.
        It dynamically calculates the highest wall to the left and right, and calculates the rainwater that can be
        trapped at each step.

        Time Complexity:
            The time complexity is O(n), where n is the number of walls. This is because we make a single pass
            through the array.

        Space Complexity:
            The space complexity is O(1), constant. This is because we only use a constant amount of variables
            and do not use any data structures that scale with input size.

        Args:
            height (List[int]): A list of non-negative integers representing the heights of the walls.

        Returns:
            int: The total amount of rainwater that can be trapped.
        """

        n = len(height)
        L, R = 0, n - 1
        tallest_left_wall, tallest_right_wall = float("-inf"), float("-inf")
        rain_trapped = 0

        while L < R:
            left_wall, right_wall = height[L], height[R]
            tallest_left_wall = max(tallest_left_wall, left_wall)
            tallest_right_wall = max(tallest_right_wall, right_wall)

            if left_wall < right_wall:
                rain_trapped += tallest_left_wall - left_wall
                L += 1
            else:
                rain_trapped += tallest_right_wall - right_wall
                R -= 1

        return rain_trapped
