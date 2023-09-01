from collections import deque

from helpers.leetcode_1490_helper import Node


class Solution:
    def cloneTree(self, root: "Node") -> "Node":
        """
        Clones an N-ary tree given its root node using an iterative approach.

        Parameters:
        - root (Node): The root node of the tree to be cloned.

        Returns:
        - Node: The root node of the cloned tree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n) for the queue and cloned tree.
        """

        # Base case: if the root is None, return None
        if not root:
            return None

        # Initialize the cloned root and the queue for BFS traversal
        cloned_root = Node(root.val)
        q = deque([(root, cloned_root)])

        # BFS traversal
        while q:
            node, cloned_node = q.popleft()

            # Clone all children of the current node
            for child in node.children:
                cloned_child = Node(child.val)
                cloned_node.children.append(cloned_child)
                q.append((child, cloned_child))

        return cloned_root
