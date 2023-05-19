from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given a list of non-negative integers representing the heights of vertical walls,
        this function calculates how much rainwater can be trapped between the walls.

        This implementation uses two arrays to keep track of the highest wall to the left and to the right
        of each wall. Then, for each wall, it calculates the rainwater it can trap by finding the minimum of
        the highest wall to its left and right and subtracting the height of the current wall.

        Time Complexity:
            The time complexity is O(n), where n is the number of walls. This is because we make one pass to
            compute the highest wall to the right of each wall, and another pass to compute the trapped rainwater.

        Space Complexity:
            The space complexity is O(n), where n is the number of walls. This is due to the storage needed for
            the array of highest walls to the right.

        Args:
            height (List[int]): A list of non-negative integers representing the heights of the walls.

        Returns:
            int: The total amount of rainwater that can be trapped.
        """

        n = len(height)

        # Calculate the highest wall to the right of each wall
        tallest_right_wall = [float("-inf")] * n
        tallest_right_wall[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            tallest_right_wall[i] = max(height[i], tallest_right_wall[i + 1])

        rain_trapped = 0
        tallest_left_wall = height[0]

        # Calculate the rainwater each wall can trap
        for i in range(1, n - 1):
            tallest_left_wall = max(tallest_left_wall, height[i])
            rain_trapped += (
                min(tallest_left_wall, tallest_right_wall[i]) - height[i]
            )

        return rain_trapped
