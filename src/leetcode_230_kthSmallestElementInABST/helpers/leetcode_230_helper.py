class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
    
class TreeHelper:
    def arr_to_tree(self, arr: list[int], root_pos= 0) -> TreeNode:
        if not arr:
            return None
        
        if root_pos >= len(arr) or arr[root_pos] is None:
            return None
        
        root = TreeNode(arr[root_pos])
        root.left = self.arr_to_tree(arr, root_pos * 2 + 1)
        root.right = self.arr_to_tree(arr, root_pos * 2 + 2)

        return root
