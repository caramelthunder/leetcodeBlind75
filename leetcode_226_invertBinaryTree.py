'''
https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Helper:
    def numbers_to_tree(self, numbers: List[int]) -> TreeNode:
        def helper(i: int) -> TreeNode:
            if i >= len(numbers) or numbers[i] is None:
                return None
            node = TreeNode(numbers[i])
            node.left = helper(i * 2 + 1)
            node.right = helper(i * 2 + 2)
            return node
        return helper(0)

    def tree_to_numbers(self, root: TreeNode) -> List[int]:
        def helper(node: TreeNode) -> List[int]:
            if not node:
                return [None]
            left_numbers = helper(node.left)
            right_numbers = helper(node.right)
            return [node.val] + left_numbers + right_numbers
        return helper(root)

class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        pass

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.solution1 = Solution1()


#################################
if __name__ == '__main__':
    unittest.main()
    
