'''
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree 
in which the depth of the two subtrees of every 
node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]

      3
    /   \
   9     20
         / \
        15  7

Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]

                  1
                /   \
               2     2
              / \   
             3   3
           /   \
          4     4

Output: false

Example 3:
Input: root = []
Output: true
 
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

class TreeNode:
   def __init__(self, val, left= None, right= None):
      self.val = val
      self.left = left
      self.right = right

from collections import deque
class Helper:
   def nums_to_tree(self, nums: list[int]) -> TreeNode:
      if not nums:
         return None

      def dfs(nums, i):
         if not nums or i >= len(nums) or nums[i] == 'null':
            return None
         
         node = TreeNode(nums[i])
         node.left = dfs(nums, i * 2 + 1)
         node.right = dfs(nums, i * 2 + 2)

         return node

      root = dfs(nums, 0)
      return root

   def tree_to_nums(self, root: TreeNode) -> list[int]:
      if not root:
         return []
      
      nums = []
      q = deque([root])
      while q:
         level_len = len(q)
         level = []
         for _ in range(level_len):
            node = q.popleft()
            if node != 'null':
               level.append(node.val)
               for child in [node.left, node.right]:
                  if child:
                     q.append(child)
                  else:
                     q.append('null')
            else:
               level.append(node)
         nums.append(level)
      return nums

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def dfs(node):
            if not node:
                return (True, 0)

            left_isBalanced, left_height = dfs(node.left)
            right_isBalanced, right_height = dfs(node.right)

            isBalanced = True
            height = max(left_height, right_height) + 1

            if not (left_isBalanced and right_isBalanced) or abs(left_height - right_height) > 1:
                isBalanced = False
            
            return (isBalanced, height)
        
        isBalanced, _ = dfs(root)
        return isBalanced
    
import unittest
class Test(unittest.TestCase):
    def setUp(self):
       self.solution = Solution()
       self.helper = Helper()
    
    def test_example_1(self):
        nums = [3,9,20,'null','null',15,7]
        expected_output = True
        actual_output = self.solution.isBalanced(
            self.helper.nums_to_tree(nums)
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        nums = [1,2,2,3,3,'null','null',4,4]
        expected_output = False
        actual_output = self.solution.isBalanced(
            self.helper.nums_to_tree(nums)
        )
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        nums = []
        expected_output = True
        actual_output = self.solution.isBalanced(
            self.helper.nums_to_tree(nums)
        )
        self.assertEqual(actual_output, expected_output)

################################
if __name__ == '__main__':
    unittest.main()
