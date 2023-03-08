from helpers.leetcode_199_helper import TreeNode
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        right_side_view = []

        q = deque([root])
        while q:
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                right_most = node.val

                for child in [node.left, node.right]:
                    if child is not None:
                        q.append(child)

            right_side_view.append(right_most)

        return right_side_view