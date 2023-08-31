from typing import Optional
from helpers.leetcode_298_helper import TreeNode


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """
        Returns the length of the longest consecutive sequence path of a binary tree.
        The path refers to any sequence of nodes from some starting node to any node in the tree
        along the parent-child connections. The longest consecutive path needs to be from parent
        to child (cannot be the reverse).

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The length of the longest consecutive sequence path.

        Time Complexity:
            O(N), where N is the number of nodes in the tree. Each node is visited only once.

        Space Complexity:
            O(H), where H is the height of the tree. This accounts for the maximum function call stack size.
        """
        self.global_lcs = 0

        def _longest_consecutive(node: TreeNode):
            if not node:
                return 0

            local_lcs = 1
            left_lcs = _longest_consecutive(node.left)
            right_lcs = _longest_consecutive(node.right)

            if node.left and node.left.val == node.val + 1:
                local_lcs = max(local_lcs, left_lcs + 1)
            if node.right and node.right.val == node.val + 1:
                local_lcs = max(local_lcs, right_lcs + 1)

            self.global_lcs = max(self.global_lcs, local_lcs)
            return local_lcs

        _longest_consecutive(root)
        lcs = self.global_lcs
        self.global_lcs = 0
        return lcs
