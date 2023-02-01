'''
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
          1
        /   \
       2     3
      /  \
     4    5
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''

class TreeNode:
  def __init__(self, val= None):
    self.val = val
    self.left = None
    self.right = None

class TreeHelper:
  def arr_to_tree(self, arr: list[any]) -> TreeNode:

    def _arr_to_tree(arr, pos= 0):
      if not arr or pos >= len(arr) or arr[pos] is None:
        return None

      node = TreeNode(arr[pos])
      node.left = _arr_to_tree(arr, pos * 2 + 1)
      node.right = _arr_to_tree(arr, pos * 2 + 2)

      return node
    return _arr_to_tree(arr, 0)

class Solution:
  def diameterOfBinaryTree(self, root: TreeNode) -> int:
    diameter = 0

    def dfs(node):
      nonlocal diameter

      if not node:
        return 0

      left_height = dfs(node.left)
      right_height = dfs(node.right)
      local_diameter = left_height + right_height
      diameter = max(diameter, local_diameter)

      return max(left_height, right_height) + 1
    
    dfs(root)
    return diameter

import unittest
class Test(unittest.TestCase):
  def setUp(self):
    self.treeHelper = TreeHelper()
    self.solution = Solution()
  
  def test_example_1(self):
    arr = [1,2,3,4,5]
    expected_output = 3
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr))
    self.assertEqual(actual_output, expected_output)

  def test_example_2(self):
    arr = [1,2]
    expected_output = 1
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr))
    self.assertEqual(actual_output, expected_output)

  def test_example_3(self):
    arr = [1,2,3,None,4,5,None]
    expected_output = 4
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr))
    self.assertEqual(actual_output, expected_output)
  
  def test_empty_tree(self):
    arr = []
    expected_output = 0
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr))
    self.assertEqual(actual_output, expected_output)

  def test_sided_tree(self):
    arr = [1,2,None,3,None,None,None,4]
    expected_output = 3
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr))
    self.assertEqual(actual_output, expected_output)

  def test_dia_in_subtree(self):
    arr = [1,None,3,None,None,4,5,None,None,None,None,None,None,None,6]
    expected_output = 3
    actual_output = self.solution.diameterOfBinaryTree(root= self.treeHelper.arr_to_tree(arr= arr))
    self.assertEqual(actual_output, expected_output)

####################################################
if __name__ == '__main__':
  unittest.main()

