'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
      6
    /   \
   2     8
  / \   / \
 0   4 7   9
    / \   
   3   5
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
      6
    /   \
   2     8
  / \   / \
 0   4 7   9
    / \   
   3   5
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
    2
   /
  1
Output: 2
 
Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
'''
class TreeNode:
   def __init__(self, val, left= None, right= None):
      self.val = val
      self.left = left
      self.right = right

from collections import deque
class Helper:
   def nums_to_tree(self, nums: list[int]) -> TreeNode:
      if not nums:
         return None

      def dfs(nums, i):
         if not nums or i >= len(nums) or nums[i] == 'null':
            return None
         
         node = TreeNode(nums[i])
         node.left = dfs(nums, i * 2 + 1)
         node.right = dfs(nums, i * 2 + 2)

         return node

      root = dfs(nums, 0)
      return root

   def tree_to_nums(self, root: TreeNode) -> list[int]:
      if not root:
         return []
      
      nums = []
      q = deque([root])
      while q:
         level_len = len(q)
         level = []
         for _ in range(level_len):
            node = q.popleft()
            if node != 'null':
               level.append(node.val)
               for child in [node.left, node.right]:
                  if child:
                     q.append(child)
                  else:
                     q.append('null')
            else:
               level.append(node)
         nums.append(level)
      return nums

class Solution_Iterative:
   def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
      if not root:
         return None
      
      node = root
      while node:

         if node.val < p.val and node.val < q.val:
            node = node.right
         elif node.val > p.val and node.val > q.val:
            node = node.left
         else:
            return node


class Solution_Recursive:
   def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

import unittest   
class Test(unittest.TestCase):
   def setUp(self):
      self.helper = Helper()
      self.solution_recursive = Solution_Recursive()
      self.solution_iterative = Solution_Iterative()
   
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