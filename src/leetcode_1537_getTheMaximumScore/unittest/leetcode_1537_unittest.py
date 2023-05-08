import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1537_solution import Solution 

class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        params = {
            'nums1': [2,4,5,8,10], 'nums2': [4,6,8,9]
        }
        expected_output = 30

        actual_output = self.sol.maxSum(nums1=params['nums1'], nums2=params['nums2'])
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = {
            'nums1': [1,3,5,7,9], 'nums2': [3,5,100]
        }
        expected_output = 109

        actual_output = self.sol.maxSum(nums1=params['nums1'], nums2=params['nums2'])
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        params = {
            'nums1': [1,2,3,4,5], 'nums2': [6,7,8,9,10]
        }
        expected_output = 40

        actual_output = self.sol.maxSum(nums1=params['nums1'], nums2=params['nums2'])
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()