from helpers.leetcode_1490_helper import Node


class Solution:
    def cloneTree(self, root: "Node") -> "Node":
        """
        Clones an N-ary tree given its root node using a recursive approach.

        Parameters:
        - root (Node): The root node of the tree to be cloned.

        Returns:
        - Node: The root node of the cloned tree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (recursion stack).
        """

        # Base case: if the root is None, return None
        if not root:
            return None

        # Initialize the cloned root
        cloned_root = Node(root.val)

        # Clone all children of the root node recursively
        for child in root.children:
            cloned_root.children.append(self.cloneTree(child))

        return cloned_root
