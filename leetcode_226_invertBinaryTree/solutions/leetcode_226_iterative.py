from helpers.leetcode_226_helper import TreeNode
from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()
            node.left, node.right = node.right , node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return root