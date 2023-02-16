class TreeNode:
    def __init__(self, val= 0):
        self.val = val
        self.left = None
        self.right = None

class TreeHelper:
    def arr_to_tree(self, arr: list[int]) -> TreeNode:
        if not arr:
            return None
        
        def dfs(arr, root_pos):
            if root_pos >= len(arr) or not arr[root_pos]:
                return None

            root = TreeNode(arr[root_pos])
            root.left = dfs(arr, root_pos * 2 + 1)
            root.right = dfs(arr, root_pos * 2 + 2)
            return root

        return dfs(arr, 0)
    