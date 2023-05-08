from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """Get the Maximum Score
        Given two sorted arrays of distinct integers nums1 and nums2.
        Calculate the maximum sum of non-intersecting subarrays from nums1 and nums2.

        Args:
            nums1 (List[int]): A sorted arrays of distinct integers.
            nums2 (List[int]): A sorted arrays of distinct integers.

        Returns:
            int: Maximum score you can obtain of all possible valid paths.

        Time complexity: O(n + m), where n and m are the lengths of nums1 and nums2, respectively.
        Space complexity: O(1), as only constant extra space is used.
        """
        MODULO = 10**9 + 7

        prefix_sum1, prefix_sum2 = 0, 0
        i1, i2, n1, n2 = 0, 0, len(nums1), len(nums2)
        max_sum = 0 

        while i1 < n1 or i2 < n2:
            if (i2 >= n2) or (i1 < n1 and nums1[i1] < nums2[i2]):
                prefix_sum1 += nums1[i1]
                i1 += 1
            elif (i1 >= n1) or (i2 < n2 and nums1[i1] > nums2[i2]):
                prefix_sum2 += nums2[i2]
                i2 += 1
            else:
                max_sum += max(prefix_sum1, prefix_sum2) + nums1[i1]
                prefix_sum1, prefix_sum2 = 0, 0
                i1 += 1
                i2 += 1

        max_sum += max(prefix_sum1, prefix_sum2)
        return max_sum % MODULO