from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Given a list of non-negative integers heights representing the histogram's bar height where the width of each bar is 1,
        this method returns the area of the largest rectangle in the histogram.

        The function employs a stack-based approach to determine the maximum area efficiently.

        Args:
            heights (List[int]): A list of integers representing the heights of bars in the histogram.

        Returns:
            int: The maximum area of the rectangle that can be formed in the histogram.

        Runtime and space complexity:
            Time(n): O(n), as each height is pushed and popped from the stack exactly once.

            Space(n): O(n), for the additional stack used.
        """
        # Initialize a stack with -1 to handle the base case
        stack = [-1]

        # This variable keeps track of the maximum rectangle area we've found so far
        max_rec_area = 0

        for i in range(len(heights)):
            # Ensure that the stack maintains increasing order of heights.
            # This loop will pop all heights from the stack that are greater than or equal to the current height.
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_rec_area = max(max_rec_area, height * width)

            # Add the current index to the stack
            stack.append(i)

        # Handle the remaining heights in the stack
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_rec_area = max(max_rec_area, height * width)

        return max_rec_area
