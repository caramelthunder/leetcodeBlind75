from collections import deque

class TreeNode:
    def __init__(self, val= None):
        self.val = val
        self.left = None
        self.right = None

class TreeHelper:
    def arr_to_tree(self, arr: list[int], root_pos= 0) -> TreeNode:
        if not arr or root_pos >= len(arr) or arr[root_pos] == None:
            return None
        
        root = TreeNode(arr[root_pos])
        root.left = self.arr_to_tree(arr, root_pos * 2 + 1)
        root.right = self.arr_to_tree(arr, root_pos * 2 + 2)

        return root
    
    def search(self, root: TreeNode, val: int) -> TreeNode:
        q = deque([root])

        while q:
            node = q.popleft()
            if node.val == val:
                return node
            for child in [node.left, node.right]:
                if child:
                    q.append(child)

        return None