from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def numbers_to_tree(numbers: List[int]) -> TreeNode:
    def helper(i: int) -> TreeNode:
        if i >= len(numbers) or numbers[i] is None:
            return None
        node = TreeNode(numbers[i])
        node.left = helper(i * 2 + 1)
        node.right = helper(i * 2 + 2)
        return node
    return helper(0)

def tree_to_numbers(root: TreeNode) -> List[int]:
    def helper(node: TreeNode) -> List[int]:
        if not node:
            return [None]
        left_numbers = helper(node.left)
        right_numbers = helper(node.right)
        return [node.val] + left_numbers + right_numbers
    return helper(root)
