'''
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
    [1] -> [2] -> [3] -> [4] -> [5]
Output: [5,4,3,2,1]
    [5] -> [4] -> [3] -> [2] -> [1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
class ListNode:
    def __init__(self, val= None):
        self.val = val
        self.next = None

class LinkedList_Helper:
    def list_to_linkedList(self, lst: list[int]) -> ListNode:
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def linkedList_to_list(self, head: ListNode) -> list[int]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst

class Solution_Recursive:
    def reverseList(self, head: ListNode) -> ListNode:
        return self._reverseList(head, None)

    def _reverseList(self,curr, tail):
        if not curr:
            return tail
        next_node = curr.next
        curr.next = tail
        return self._reverseList(next_node, curr)

class Solution_Iterative:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        tail = None

        while curr:
            next_node = curr.next
            curr.next = tail
            tail = curr
            curr = next_node
        return tail

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.linkedList_helper = LinkedList_Helper()
    
    def test_example_1(self):
        head = [1,2,3,4,5]
        expected_output = [5,4,3,2,1]

        solution1 = Solution_Recursive()
        actual_ouput1 = solution1.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput1), expected_output)
 
        solution2 = Solution_Iterative()
        actual_ouput2 = solution2.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput2), expected_output)

    def test_example_2(self):
        head = [1,2]
        expected_output = [2,1]

        solution1 = Solution_Recursive()
        actual_ouput1 = solution1.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput1), expected_output)

        solution2 = Solution_Iterative()
        actual_ouput2 = solution2.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput2), expected_output)

    def test_single_node(self):
        head = [1]
        expected_output = [1]

        solution1 = Solution_Recursive()
        actual_ouput1 = solution1.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput1), expected_output)

        solution2 = Solution_Iterative()
        actual_ouput2 = solution2.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput2), expected_output)

    def test_empty_list(self):
        head = []
        expected_output = []

        solution1 = Solution_Recursive()
        actual_ouput1 = solution1.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput1), expected_output)

        solution2 = Solution_Iterative()
        actual_ouput2 = solution2.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput2), expected_output)

##########################################
if __name__ == '__main__':
    unittest.main()