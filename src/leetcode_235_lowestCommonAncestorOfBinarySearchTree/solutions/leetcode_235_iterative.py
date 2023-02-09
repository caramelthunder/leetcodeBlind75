from helpers.leetcode_235_helper import TreeNode

class Solution:
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