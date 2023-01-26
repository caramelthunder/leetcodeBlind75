'''
https://leetcode.com/problems/linked-list-cycle/
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 
Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

class LinkedList:
    def __init__(self, val= None, next= None):
        self.val = val
        self.next = next
    
class Helper: 
    def arr_to_list(self, arr: list[int], cycle_pos= -1) -> LinkedList:
        nodes_map = {}

        dummy = LinkedList()
        node = dummy

        for i in range(len(arr)):
            val = arr[i]
            new_node = LinkedList(val)
            nodes_map[i] = new_node

            node.next = new_node
            node = node.next
        
        if cycle_pos in nodes_map:
            node.next = nodes_map[cycle_pos]
        
        return dummy.next

class Solution:
    def hasCycle(self, head: LinkedList) -> bool:
        slow, fast = head, head
        at_start = True

        while fast and fast.next:
            if not at_start and slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
            at_start = False

        return False

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.solution = Solution()

    def test_example_1(self):
        head = [3,2,0,-4]
        pos = 1
        expected_output = True
        actual_output = self.solution.hasCycle(self.helper.arr_to_list(head, pos))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        head = [1,2]
        pos = 0
        expected_output = True
        actual_output = self.solution.hasCycle(self.helper.arr_to_list(head, pos))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        head = [1]
        pos = -1
        expected_output = False
        actual_output = self.solution.hasCycle(self.helper.arr_to_list(head, pos))
        self.assertEqual(actual_output, expected_output)

########################################
if __name__ == '__main__':
    unittest.main()