import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
 
from solutions.leetcode_104_solution import Solution
from helpers.leetcode_104_helper import TreeHelper
import unittest

class Test(unittest.TestCase):
    def setUp(self):  
        self.treeHelper = TreeHelper()
        self.solution = Solution()
  
    def test_example_1(self):
        arr = [3,9,20,None,None,15,7]
        expected_output = 3
        actual_output = self.solution.maxDepth(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        arr = [1,None,2]
        expected_output = 2
        actual_output = self.solution.maxDepth(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_1(self):
        arr = []
        expected_output = 0
        actual_output = self.solution.maxDepth(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_2(self):
        arr = [0]
        expected_output = 1
        actual_output = self.solution.maxDepth(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_3(self):
        arr = [100, 99, 98, 97, 96, 95]
        expected_output = 3
        actual_output = self.solution.maxDepth(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
        self.assertEqual(actual_output, expected_output)

    def test_different_shapes_1(self):
        arr = [1, 2, 3, 4, None, None, 7]
        expected_output = 3
        actual_output = self.solution.maxDepth(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
        self.assertEqual(actual_output, expected_output)


###########################################
if __name__ == '__main__':
  unittest.main()
    