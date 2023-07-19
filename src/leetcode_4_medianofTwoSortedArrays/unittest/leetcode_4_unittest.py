import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_4_naive import Solution as NaiveSolution
from solutions.leetcode_4_binary_search import Solution as BinarySearch
from solutions.leetcode_4_better_binary_search import Solution as BetterBinarySearch


class Test(unittest.TestCase):
    def setUp(self):
        self.naive_solution = NaiveSolution()
        self.binary_search = BinarySearch()
        self.better_binary_search = BetterBinarySearch()

    def test_findMedianSortedArrays(self):
        # test cases for the naive solution
        test_cases = (
            ([1, 3], [2], 2.0),
            ([1, 2], [3, 4], 2.5),
            ([0, 0], [0, 0], 0.0),
            ([], [1], 1.0),
            ([2], [], 2.0),
        )

        for nums1, nums2, expected in test_cases:
            with self.subTest(nums1=nums1, nums2=nums2, expected=expected):
                self.assertEqual(self.naive_solution.findMedianSortedArrays(nums1, nums2), expected)
                self.assertEqual(self.binary_search.findMedianSortedArrays(nums1, nums2), expected)
                self.assertEqual(self.better_binary_search.findMedianSortedArrays(nums1, nums2), expected)


######################################
if __name__ == '__main__':
    unittest.main()