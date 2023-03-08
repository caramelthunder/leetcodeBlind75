class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeHelper:
    def arr_to_tree(self, arr: list[int], root_pos= 0) -> TreeNode:
        if not arr:
            return None
        
        if root_pos >= len(arr) or not arr[root_pos]:
            return None
        
        tree = TreeNode(arr[root_pos])
        tree.left = self.arr_to_tree(arr, root_pos * 2 + 1)
        tree.right = self.arr_to_tree(arr, root_pos * 2 + 2)

        return tree
'''
Example 1:

         1
       /   \
      2     3
       \     \
        5     4

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
'''