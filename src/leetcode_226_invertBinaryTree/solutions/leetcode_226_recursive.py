from helpers.leetcode_226_helper import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)

        root.left = right_tree
        root.right = left_tree

        return root