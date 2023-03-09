from helpers.leetcode_105_helper import TreeNode

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not (preorder and inorder):
            return None
        
        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        tree = TreeNode(root_val)

        tree.left = self.buildTree(
            preorder= preorder[1: root_idx + 1],
            inorder= inorder[: root_idx]
        )

        tree.right = self.buildTree(
            preorder= preorder[root_idx + 1:],
            inorder= inorder[root_idx + 1:]
        )

        return tree
        