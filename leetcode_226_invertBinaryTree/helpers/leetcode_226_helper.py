from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeHelper:
    def numbers_to_tree(self, numbers: List[int]) -> TreeNode:
        if not numbers:
            return None
        nodes = iter(numbers)
        root = TreeNode(next(nodes))
        queue = [root]
        while queue:
            node = queue.pop(0)
            left_tree = next(nodes, None)
            if left_tree:
                node.left = TreeNode(left_tree)
                queue.append(node.left)

            right_tree = next(nodes, None)
            if right_tree:
                node.right = TreeNode(right_tree)
                queue.append(node.right)
        return root

    def tree_to_numbers(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        numbers = []
        while queue:
            node = queue.pop(0)
            numbers.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return numbers