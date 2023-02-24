from helpers.leetcode_236_helper import TreeNode

class Solution:
	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		if not root:
			return None
		
		path_to_p = self.get_path(root, p)
		path_to_q = self.get_path(root, q)
		
		for node in reversed(path_to_q):
			if node in set(path_to_p):
				return node
		return None

	def get_path(self, node: TreeNode, target: TreeNode) -> list[TreeNode]:
		if not node:
			return []
		
		if node == target:
			return [node]
		
		path = [node]
		for child in [node.left, node.right]:
			child_path = self.get_path(child, target)
			if child_path:
				return path + child_path
		return []

