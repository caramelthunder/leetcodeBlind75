from helpers.leetcode_102_helper import TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        
        levels = []
        q = deque([(root, 0)])
        while q:
            level_len = len(q)
            levels.append([])
            for _ in range(level_len):
                node, lv = q.popleft()
                levels[lv].append(node.val)

                if node.left:
                    q.append((node.left, lv + 1))   
                if node.right:
                    q.append((node.right, lv + 1))

        return levels