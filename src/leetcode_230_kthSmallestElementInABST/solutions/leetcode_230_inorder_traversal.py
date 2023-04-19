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

        Traverses the binary search tree rooted at `node` in-order and appends the
        values of its nodes to `inorder`, stopping when `inorder` has length `k` or
        all nodes have been visited.

        Args:
            root (TreeNode): The root node of the binary search tree.
            k (int): The index of the value to be returned (1-indexed).

        Returns:
            int: The kth smallest value in the binary search tree.

        Time Complexity:
        The time complexity of the _traverse method is O(n), where n is the number of nodes in the binary search tree. This is because the method visits each node in the tree exactly once.
        The time complexity of the kthSmallest method is also O(n), since it calls the _traverse method, which has a time complexity of O(n).
        Overall, the time complexity of the solution is O(n).

        Space Complexity:

        The space complexity of the _traverse method is O(k), where k is the input parameter representing the index of the value to be returned (1-indexed). This is because the method appends the values of the nodes to the inorder list only if its length is less than k. In the worst case, inorder will have length k, so the space complexity is O(k).
        The space complexity of the kthSmallest method is O(k) as well, since it initializes an empty inorder list, which has a maximum length of k.
        Overall, the space complexity of the solution is O(k).

        """
        
        def _traverse(node):
            if node:
                _traverse(node.left)

                if len(inorder) < k:
                    inorder.append(node.val)
                    _traverse(node.right)
                    

        inorder = []
        _traverse(root)
        return inorder[k - 1]

    

        
        