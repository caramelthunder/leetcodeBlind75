from helpers.leetcode_543_helper import TreeNode

class Solution:
  def diameterOfBinaryTree(self, root: TreeNode) -> int:
    def dfs(node):
      if not node:
        return (0, 0)

      left_dia, left_height = dfs(node.left)
      right_dia, right_height = dfs(node.right)
      local_diameter = left_height + right_height

      diameter = max(max(left_dia, right_dia), local_diameter)

      return (diameter, max(left_height, right_height) + 1)
    
    diameter, _ = dfs(root)
    return diameter