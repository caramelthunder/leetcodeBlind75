class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class TreeHelper:
    def arr_to_tree(self, arr: list[int], pos= 0):
        if not arr:
            return None
        
        def _helper(data, root_pos= 0):
            if root_pos >= len(data) or data[root_pos] == 'null':
                return None
            
            root = TreeNode(data[root_pos])
            root.left = _helper(data, root_pos * 2 + 1)
            root.right = _helper(data, root_pos * 2 + 2)

            return root
        
        return _helper(arr)
    
    def tree_to_arr(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        arr = []
        q = deque([root])
        while q:
            node = q.popleft()
            arr.append(int(node.val)if node else 'null')
            if node:
                for child in [node.left, node.right]:
                    q.append(child)
            
        while arr[-1] == 'null':
            arr.pop()
        
        return arr