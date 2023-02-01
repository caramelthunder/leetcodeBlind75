'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
           3
         /   \
        9     20
             /   \
            15    7
Output: 3

Example 2:
Input: root = [1,null,2]
          1
           \ 
            2
Output: 2
 
Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
class TreeNode:
  def __init__(self, val= None):
    self.val = val
    self.left = None
    self.right = None

class TreeHelper:
  def arr_to_tree(self, arr: list[any], pos: int) -> TreeNode:
    if not arr or pos >= len(arr) or arr[pos] is None:
      return None

    node = TreeNode(arr[pos])
    node.left = self.arr_to_tree(arr, pos * 2 + 1)
    node.right = self.arr_to_tree(arr, pos * 2 + 2)

    return node

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
          return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1

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

###########################################
if __name__ == '__main__':
  unittest.main()
    