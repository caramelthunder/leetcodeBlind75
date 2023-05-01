# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:
    def serialize(self, root):
        """
        Encodes a binary tree to a single string using pre-order traversal.
        
        :param root: The root TreeNode of the binary tree.
        :type root: TreeNode
        :return: Serialized binary tree as a comma-separated string.
        :rtype: str

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree (O(n) in the worst case).
        """

        if not root:
            return ''

        def _helper(node):
            if not node:
                return "null"

            tree = str(node.val)
            tree += "," + _helper(node.left)
            tree += "," + _helper(node.right)

            return tree

        return _helper(root)

    def deserialize(self, data):
        """
        Decodes the encoded data to construct a binary tree.
        
        :param data: Serialized binary tree as a comma-separated string.
        :type data: str
        :return: The root TreeNode of the reconstructed binary tree.
        :rtype: TreeNode

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n) for the deque and O(h) for the call stack, where h is the height of the tree (O(n) in the worst case).
        """

        if data == '':
            return None

        nodes = deque([val for val in data.split(',')])

        def _helper(nodes):
            root_val = nodes.popleft()

            if root_val == "null":
                return None
            
            root = TreeNode(root_val)
            root.left = _helper(nodes)
            root.right = _helper(nodes)

            return root
        
        return _helper(nodes)
