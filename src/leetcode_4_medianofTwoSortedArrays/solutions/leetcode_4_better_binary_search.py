class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Finds the median of two sorted integer arrays.

        This function applies a binary search algorithm and array partitioning technique
        to efficiently find the median value. It assumes the first list (nums1) is smaller
        or equal in size to the second list (nums2). If not, it swaps the two lists. It
        operates on the smaller list to ensure the binary search is performed on the smaller array,
        hence optimizing the time complexity.

        Args:
            nums1 (list[int]): The first input list of integers, sorted in ascending order.
            nums2 (list[int]): The second input list of integers, sorted in ascending order.

        Returns:
            float: The median of the combined input lists. If the total length of the combined lists
                   is even, it returns the average of the two middle elements. If it is odd,
                   it returns the single middle element.
        """
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        # assume nums1(m) is smaller than or equal to nums2(n), else swap the two arrays.
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # Operating on the smaller array.
        left, right = 0, m
        
        while left <= right:
            # Determine the partitions in both arrays such that all elements in the left partitions 
            # are less than or equal to elements in the right partitions.
            partition_m = left + (right - left) // 2
            partition_n = half - partition_m
            
            # Compute the border elements for each partition. 
            # If a partition has no elements, use -inf/inf as needed.
            max_left_m = nums1[partition_m - 1] if partition_m > 0 else float('-inf')
            min_right_m = nums1[partition_m] if partition_m < m else float('inf')
            max_left_n = nums2[partition_n - 1] if partition_n > 0 else float('-inf')
            min_right_n = nums2[partition_n] if partition_n < n else float('inf')

            # Check if the correct partitions are found.
            # If the largest elements of the left halves are less than or equal to 
            # the smallest elements of the right halves, the correct partitions are found.
            if max_left_m <= min_right_n and max_left_n <= min_right_m:
                # If the total length of the combined arrays is even, return the average of 
                # the maximum element in the left partition and the minimum element in the right partition.
                # If the total length is odd, return the maximum element in the left partition.
                if (m + n) % 2 == 0:
                    return (max(max_left_m, max_left_n) + min(min_right_m, min_right_n)) / 2
                else:
                    return max(max_left_m, max_left_n)
            # If the correct partitions are not found, update the binary search range.
            # If max_left_m is larger than min_right_n, move right to partition_m. 
            # Else, move left to partition_m + 1.
            elif max_left_m > min_right_n:
                right = partition_m
            else:
                left = partition_m + 1
        







        