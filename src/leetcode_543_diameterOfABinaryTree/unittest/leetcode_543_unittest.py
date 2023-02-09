import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_543_helper import TreeHelper
from solutions.leetcode_543_solution import Solution

class Test(unittest.TestCase):
  def setUp(self):
    self.treeHelper = TreeHelper()
    self.solution = Solution()
  
  def test_example_1(self):
    arr = [1,2,3,4,5]
    expected_output = 3
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
    self.assertEqual(actual_output, expected_output)

  def test_example_2(self):
    arr = [1,2]
    expected_output = 1
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
    self.assertEqual(actual_output, expected_output)

  def test_example_3(self):
    arr = [1,2,3,None,4,5,None]
    expected_output = 4
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
    self.assertEqual(actual_output, expected_output)
  
  def test_empty_tree(self):
    arr = []
    expected_output = 0
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
    self.assertEqual(actual_output, expected_output)

  def test_sided_tree(self):
    arr = [1,2,None,3,None,None,None,4]
    expected_output = 3
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
    self.assertEqual(actual_output, expected_output)

  def test_dia_in_subtree(self):
    arr = [1,None,3,None,None,4,5,None,None,None,None,None,None,None,6]
    expected_output = 3
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr, pos= 0))
    self.assertEqual(actual_output, expected_output)

####################################################
if __name__ == '__main__':
  unittest.main()


