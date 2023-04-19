class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Returns the kth smallest value in the binary search tree rooted at `root`.
        Assumes that `k` is a valid index (i.e., 1 <= k <= number of nodes in tree).

        Args:
            root (TreeNode): The root node of the binary search tree.
            k (int): The index of the value to be returned (1-indexed).

        Returns:
            int: The kth smallest value in the binary search tree.

        The time complexity: O(n) in the worst case, 
        where n is the number of nodes in the binary search tree. 
        This is because the algorithm visits each node in the tree exactly once.

        The space complexity: O(h) in the worst case, 
        where h is the height of the binary search tree. 
        This is because the size of the stack is proportional to the height of the tree, 
        which can be as large as n in the worst case if the tree is unbalanced. 
        However, if the tree is balanced, the height is O(log n) and the space complexity is O(log n).

        """
        stack = []  # stack for iterative in-order traversal
        count = 0   # counter for tracking number of visited nodes
        node = root # start at root node
        
        while stack or node:
            # Traverse left subtree until we reach the leftmost leaf node
            if node:
                stack.append(node)
                node = node.left
            # Pop the last node from the stack and visit it
            else:
                node = stack.pop()
                count += 1
                # Check if the kth smallest value has been found
                if count == k:
                    return node.val
                # Traverse the right subtree of the current node
                node = node.right
        
        # If we reach this point, kth smallest value was not found
        return None
