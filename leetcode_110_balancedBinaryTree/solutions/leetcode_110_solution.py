from helpers.leetcode_110_helper import TreeNode

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def dfs(node):
            if not node:
                return (True, 0)

            left_isBalanced, left_height = dfs(node.left)
            right_isBalanced, right_height = dfs(node.right)

            isBalanced = True
            height = max(left_height, right_height) + 1

            if not (left_isBalanced and right_isBalanced) or abs(left_height - right_height) > 1:
                isBalanced = False
            
            return (isBalanced, height)
        
        isBalanced, _ = dfs(root)
        return isBalanced