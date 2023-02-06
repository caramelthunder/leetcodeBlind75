from helpers.leetcode_102_helper import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        levels = []
        self.dfs(root, levels, 0)
        return levels

    def dfs(self, node,levels, lv= 0):
        if not node:
            return

        if len(levels) <= lv:
            levels.append([])
        
        levels[lv].append(node.val)
        self.dfs(node.left, levels, lv + 1)
        self.dfs(node.right, levels, lv + 1)
        
