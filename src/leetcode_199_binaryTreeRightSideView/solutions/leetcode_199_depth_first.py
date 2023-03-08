from helpers.leetcode_199_helper import TreeNode

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        right_side_view = []
        self._rightSideView(root, right_side_view, 0)
        return right_side_view
    
    def _rightSideView(self, node, right_side_view, curr_lv= 0):
        if len(right_side_view) <= curr_lv:
            right_side_view.append(None)
        
        right_side_view[curr_lv] = node.val

        if node.left:
            self._rightSideView(node.left, right_side_view, curr_lv + 1)
        if node.right:
            self._rightSideView(node.right, right_side_view, curr_lv + 1)