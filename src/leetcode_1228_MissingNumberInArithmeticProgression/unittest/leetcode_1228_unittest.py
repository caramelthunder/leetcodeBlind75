import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1228_binary_search import Solution as BinarySearch
from solutions.leetcode_1228_linear_search import Solution as LinearSearch

class Test(unittest.TestCase):
    def setUp(self):
        self.binary_search = BinarySearch()
        self.linear_search = LinearSearch()
    
    def test_example_1(self):
        arr = [5, 7, 11, 13]
        expected_output = 9

        actual_output = self.binary_search.missingNumber(arr)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.linear_search.missingNumber(arr)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        arr = [15,13,12]
        expected_output = 14

        actual_output = self.binary_search.missingNumber(arr)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.linear_search.missingNumber(arr)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()


'''
Example 1:
Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].

Example 2:
Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].
'''
