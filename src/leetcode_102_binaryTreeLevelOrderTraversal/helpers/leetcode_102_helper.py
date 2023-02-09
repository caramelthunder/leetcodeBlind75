class TreeNode:
  def __init__(self, val= None):
    self.val = val
    self.left = None
    self.right = None

class TreeHelper:
  def arr_to_tree(self, arr: list[any], pos: int) -> TreeNode:
    if not arr or pos >= len(arr) or arr[pos] is None:
      return None

    node = TreeNode(arr[pos])
    node.left = self.arr_to_tree(arr, pos * 2 + 1)
    node.right = self.arr_to_tree(arr, pos * 2 + 2)

    return node
