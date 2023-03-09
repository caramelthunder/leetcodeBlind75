from helpers.leetcode_105_helper import TreeNode

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        PS, PE = 0, len(preorder) - 1
        IS, IE = 0, len(inorder) - 1
        idx_lookup = {val: i for i, val in enumerate(inorder)}

        return self._buildTree(preorder, PS, PE, inorder, IS, IE, idx_lookup)
    
    def _buildTree(self, preorder, PS, PE, inorder, IS, IE, idx_lookup):
        if PS > PE or IS > IE:
            return None
        
        root_val = preorder[PS]
        root_idx = idx_lookup[root_val]
        left_tree_len = root_idx - IS
        right_tree_len = IE - root_idx

        tree = TreeNode(root_val)

        tree.left = self._buildTree(
            preorder, PS + 1, PS + left_tree_len, 
            inorder, IS, root_idx - 1, 
            idx_lookup
        )

        tree.right = self._buildTree(
            preorder, PE - right_tree_len + 1, PE, 
            inorder, root_idx + 1, IE, 
            idx_lookup
        )

        return tree