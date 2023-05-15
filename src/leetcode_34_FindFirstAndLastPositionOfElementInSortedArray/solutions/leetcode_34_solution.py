from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given a sorted list, this function returns the starting and ending position of a given target value.
        If the target is not found in the list, it returns [-1, -1].

        Args:
            nums (List[int]): Sorted list of integers.
            target (int): The target value to find in the list.

        Returns:
            List[int]: A list of two integers representing the starting and ending positions of the target value.

        Time Complexity:
            O(log n): Since we're using a binary search, the time complexity is logarithmic.
                      We are essentially halving the search space at each step until we find the target.

        Space Complexity:
            O(1): The space complexity is constant as we are not using any additional data structures
                  whose size depends on the input. We are only using a few integer variables.
        """
        n = len(nums)

        start_i = self._binary_search(nums, 0, n - 1, target, False)

        if start_i == (-1):
            return [-1, -1]

        end_i = self._binary_search(nums, start_i, n - 1, target, True)
        return [start_i, end_i]

    def _binary_search(self, nums, left, right, target, start_found):
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if start_found is not True:
                    if mid == left or nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                else:  # looking for end_i.
                    if mid == right or nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid + 1
        return -1
