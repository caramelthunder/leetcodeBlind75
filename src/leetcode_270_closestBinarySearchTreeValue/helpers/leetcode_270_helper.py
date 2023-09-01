class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeHelpers:
    def arr_to_tree(self, arr: list[int], root_pos=0) -> TreeNode:
        if not arr or root_pos >= len(arr) or arr[root_pos] is None:
            return None

        root = TreeNode(arr[root_pos])
        root.left = self.arr_to_tree(arr, root_pos * 2 + 1)
        root.right = self.arr_to_tree(arr, root_pos * 2 + 2)
        return root

    def tree_to_arr(self, root: TreeNode) -> list[int]:
        return []
