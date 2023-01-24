'''
https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
         4
       /   \
      2     7
     / \   / \
    1   3 6   9

Output: [4,7,2,9,6,3,1]
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

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
        if not numbers:
            return None
        root = TreeNode(numbers[0])
        queue = [root]
        i = 1
        while queue and i < len(numbers):
            node = queue.pop(0)
            if numbers[i] is not None:
                node.left = TreeNode(numbers[i])
                queue.append(node.left)
            i += 1
            if i < len(numbers) and numbers[i] is not None:
                node.right = TreeNode(numbers[i])
                queue.append(node.right)
            i += 1
        return root

    def tree_to_numbers(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        numbers = []
        while queue:
            node = queue.pop(0)
            numbers.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return numbers

class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return root

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.solution1 = Solution1()

    def test_example1(self):
        params = self.helper.numbers_to_tree([4,2,7,1,3,6,9])
        expected_output = [4,7,2,9,6,3,1]
        actual_output1 = self.helper.tree_to_numbers(self.solution1.invertTree(params))
        self.assertEqual(actual_output1, expected_output)

#################################
if __name__ == '__main__':
    unittest.main()
    
