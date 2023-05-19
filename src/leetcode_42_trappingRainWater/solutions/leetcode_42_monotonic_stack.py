from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given a list of non-negative integers representing the elevation of a vertical wall,
        this function calculates how much rainwater can be trapped between the walls.

        The method uses a stack to keep track of the walls. It traverses the wall heights from left to right,
        and while the stack is not empty and the current wall's height is greater than the height of the wall
        at the top of the stack, it calculates the rainwater trapped.

        Time Complexity:
            The time complexity is O(n), where n is the number of walls.
            This is because we process each wall once.

        Space Complexity:
            The space complexity is O(n), where n is the number of walls.
            In the worst case scenario, we may end up pushing all the walls onto the stack.

        Args:
            height (List[int]): A list of non-negative integers representing the heights of the walls.

        Returns:
            int: The total amount of rainwater that can be trapped.
        """

        stack = []
        rain_trapped = 0

        for i, right_wall in enumerate(height):
            while stack and height[stack[-1]] < right_wall:
                floor = height[stack.pop()]

                if stack:
                    left_wall = height[stack[-1]]
                else:
                    break

                left_right_dist = i - stack[-1] - 1
                height_offset = min(left_wall, right_wall) - floor
                rain_trapped += height_offset * left_right_dist

            stack.append(i)

        return rain_trapped
