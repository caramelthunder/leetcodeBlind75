import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_496_solution import Solution 

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1, nums2 = [4,1,2], [1,3,4,2]
        expected_output = [-1, 3, -1]

        actual_output = self.solution.nextGreaterElement(nums1= nums1, nums2= nums2)
        self.assertEqual(actual_output, expected_output)
######################################
if __name__ == '__main__':
    unittest.main()

'''
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
'''