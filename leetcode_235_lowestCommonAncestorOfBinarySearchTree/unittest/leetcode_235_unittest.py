import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_235_helper import TreeHelper, TreeNode
from solutions.leetcode_235_iterative import Solution as Solution1
from solutions.leetcode_235_recursive import Solution as Solution2

class Test(unittest.TestCase):
   def setUp(self):
      self.helper = TreeHelper()
      self.solution_recursive = Solution1()
      self.solution_iterative = Solution2()
   
   def test_example_1(self):
      nums = [6,2,8,0,4,7,9,'null','null',3,5]
      p, q = 2, 8
      expected_output = 6

      actual_output_recursive = self.solution_recursive.lowestCommonAncestor(
         self.helper.nums_to_tree(nums), 
         TreeNode(p), 
         TreeNode(q)
         ).val
      self.assertEqual(actual_output_recursive, expected_output)

      actual_output_iterative = self.solution_iterative.lowestCommonAncestor(
         self.helper.nums_to_tree(nums), 
         TreeNode(p), 
         TreeNode(q)
         ).val
      self.assertEqual(actual_output_iterative, expected_output)

   def test_example_2(self):
      nums = [6,2,8,0,4,7,9,'null','null',3,5]
      p, q = 2, 4
      expected_output = 2

      actual_output_recursive = self.solution_recursive.lowestCommonAncestor(
         self.helper.nums_to_tree(nums), 
         TreeNode(p), 
         TreeNode(q)
         ).val
      self.assertEqual(actual_output_recursive, expected_output)

      actual_output_iterative = self.solution_iterative.lowestCommonAncestor(
         self.helper.nums_to_tree(nums), 
         TreeNode(p), 
         TreeNode(q)
         ).val
      self.assertEqual(actual_output_iterative, expected_output)

   def test_example_3(self):
      nums = [2,1]
      p, q = 2, 1
      expected_output = 2

      actual_output_recursive = self.solution_recursive.lowestCommonAncestor(
         self.helper.nums_to_tree(nums), 
         TreeNode(p), 
         TreeNode(q)
         ).val
      self.assertEqual(actual_output_recursive, expected_output)

      actual_output_iterative = self.solution_iterative.lowestCommonAncestor(
         self.helper.nums_to_tree(nums), 
         TreeNode(p), 
         TreeNode(q)
         ).val
      self.assertEqual(actual_output_iterative, expected_output)

#############################################
if __name__ == '__main__':
   unittest.main()