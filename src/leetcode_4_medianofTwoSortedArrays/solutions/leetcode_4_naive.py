from typing import List


class Solution:
    """
    Finds the median of two sorted integer arrays.

    This function applies a merging-like procedure to find the median. It compares the
    elements of both arrays in order, discarding elements that are less than the median
    until the median or medians (in the case of even total length) are found.

    Args:
        nums1 (List[int]): The first input list of integers, sorted in ascending order.
        nums2 (List[int]): The second input list of integers, sorted in ascending order.

    Returns:
        float: The median of the combined input lists. If the total length of the combined lists
                is even, it returns the average of the two middle elements. If it is odd,
                it returns the single middle element.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Initialize pointers for each list and their lengths
        i1, i2, n1, n2 = 0, 0, len(nums1), len(nums2)

        # Helper function that advances the pointer of the list with the smaller current element 
        # and returns this smaller value
        def _get_smaller(i1, i2) -> tuple[int, int, int]:
            # Get the next values from nums1 and nums2
            # Use float('inf') as a default value if we've already iterated through the entire list
            num1 = nums1[i1] if i1 < n1 else float('inf')
            num2 = nums2[i2] if i2 < n2 else float('inf')

            # Return the smaller of the two values, along with the updated indices
            if num1 < num2:
                return (num1, i1 + 1, i2)
            else:
                return (num2, i1, i2 + 1)

        # Total number of elements in both arrays
        n = n1 + n2
        
        # If there's only one element in total, return it
        if n == 1:
            return (nums1 + nums2)[0]
            
        # Discard the values before the median by iterating through half of the total length - 1
        for _ in range(n // 2 - 1):
            _, i1, i2 = _get_smaller(i1, i2)

        # The two potential median elements will be the next two elements in the merged array
        # If the total number of elements is even, the median is the average of these two elements
        # If it's odd, the median is the second of these two elements
        median_1, i1, i2 = _get_smaller(i1, i2)
        median_2, _, _ = _get_smaller(i1, i2)
        return (median_1 + median_2) / 2 if n % 2 == 0 else median_2