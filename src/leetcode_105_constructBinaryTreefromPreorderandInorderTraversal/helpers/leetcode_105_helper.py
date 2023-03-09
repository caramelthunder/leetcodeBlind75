class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        
from collections import deque   
class TreeHelper:
    def arr_to_tree(self, arr: list[int], root_idx= 0) -> TreeNode:
        if not arr:
            return None
        
        if root_idx >= len(arr) or arr[root_idx] is None:
            return None
        
        tree = TreeNode(arr[root_idx])
        tree.left = self.arr_to_tree(arr, root_idx= root_idx * 2 + 1)
        tree.right = self.arr_to_tree(arr, root_idx= root_idx * 2 + 2)

        return tree
    
    def tree_to_arr(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        arr = []
        q = deque([root])
        while q:
            node = q.popleft()
            arr.append(node.val if node else None)
            if node:
                for child in [node.left, node.right]:
                    q.append(child)
            
        while not arr[-1]:
            arr.pop()
        
        return arr