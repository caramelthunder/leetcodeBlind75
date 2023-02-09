import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_876_helper import LinkedListHelper
from solutions.leetcode_876_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.linkedListHelper = LinkedListHelper()
        self.solution = Solution()
    
    def test_example_1(self):
        arr = [1,2,3,4,5]
        expected_output = [3,4,5]
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)

    def test_example_2(self):
        arr = [1,2,3,4,5,6]
        expected_output = [4,5,6]
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)

    def test_empty_list(self):
        arr = []
        expected_output = []
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)

    def test_single_val(self):
        arr = [1]
        expected_output = [1]
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)
    
    def test_two_val(self):
        arr = [1, 2]
        expected_output = [2]
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)

##############################
if __name__ == '__main__':
    unittest.main()
    