from typing import Optional

from helpers.leetcode_270_helper import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Finds the closest value in a Binary Search Tree (BST) to a given target using recursion.

        Time Complexity: O(H), where H is the height of the tree.
        Space Complexity: O(H), due to recursion stack.

        Args:
            root (Optional[TreeNode]): The root of the BST.
            target (float): The target value.

        Returns:
            int: The closest value to the target in the BST.
        """

        def _closest_value(node, target):
            if not node:
                return float("inf")

            # Candidate values for the closest node.
            candidates = [node.val]

            if node.val < target:
                candidates.append(_closest_value(node.right, target))
            else:
                candidates.append(_closest_value(node.left, target))

            closest_val = min(
                candidates, key=lambda val: (abs(target - val), val)
            )
            return closest_val

        closest = _closest_value(root, target)
        return closest
