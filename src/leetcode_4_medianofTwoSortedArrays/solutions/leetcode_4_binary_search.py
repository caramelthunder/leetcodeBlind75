from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted integer arrays.

        This function applies a recursive binary search to find the median.
        It compares the middle elements of the remaining parts of both arrays in each recursion
        and eliminates the half part that doesn't contain the median.

        Args:
            nums1 (List[int]): The first input list of integers, sorted in ascending order.
            nums2 (List[int]): The second input list of integers, sorted in ascending order.

        Returns:
            float: The median of the combined input lists. If the total length of the combined lists
                   is even, it returns the average of the two middle elements. If it is odd,
                   it returns the single middle element.
        """
        def solve(k: int, left_1, right_1, left_2, right_2):
            # Base cases: when one array is exhausted, return the k-th element from the other array.
            if left_1 > right_1:
                return nums2[k - left_1]
            if left_2 > right_2:
                return nums1[k - left_2]

            # Calculate the middle indices and get the middle values of remaining parts.
            i1, i2 = left_1 + (right_1 - left_1) // 2, left_2 + (right_2 - left_2) // 2
            value_1, value_2 = nums1[i1], nums2[i2]

            # Depending on the values and indices, discard the left half of the larger array or
            # the right half of the smaller array, and continue with the new sub-problem.
            if i1 + i2 < k:
                if value_1 < value_2:
                    return solve(k, i1 + 1, right_1, left_2, right_2)
                else:
                    return solve(k, left_1, right_1, i2 + 1, right_2)
            else:
                if value_1 < value_2:
                    return solve(k, left_1, right_1, left_2, i2 - 1)
                else:
                    return solve(k, left_1, i1 - 1, left_2, right_2)

        # Compute the size of the two arrays and the middle index.
        n1, n2 = len(nums1), len(nums2)
        k = (n1 + n2) // 2

        # If the total length is even, return the average of the two middle elements.
        # If the total length is odd, return the single middle element.
        if (n1 + n2) % 2 == 0:
            median_1 = solve(k - 1, 0, n1 - 1, 0, n2 - 1)
            median_2 = solve(k, 0, n1 - 1, 0, n2 - 1)
            return (median_1 + median_2) / 2
        else:
            median = solve(k, 0, n1 - 1, 0, n2 - 1)
            return median

        







        