from typing import Optional

from helpers.leetcode_270_helper import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Finds the closest value in a BST to a given target using an iterative approach.

        Time Complexity: O(H), where H is the height of the tree.
        Space Complexity: O(1), only constant extra space is used.

        Args:
            root (Optional[TreeNode]): The root of the BST.
            target (float): The target value.

        Returns:
            int: The closest value to the target in the BST.
        """
        closest_val = root.val

        while root:
            closest_val = min(
                [closest_val, root.val],
                key=lambda val: (abs(target - val), val),
            )
            root = root.left if target < root.val else root.right

        return closest_val
