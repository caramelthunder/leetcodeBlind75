'''
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
    [1] -> [2] -> [3] -> [4] -> [5]
Output: [3,4,5]
    [3] -> [4] -> [5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
class LinkedList:
    def __init__(self, val= None):
        self.val = val
        self.next = None

class LinkedListHelper:
    def arr_to_linkedList(self, arr: list[int]) -> LinkedList:
        dummy = LinkedList()
        curr = dummy
        for val in arr:
            curr.next = (LinkedList(val))
            curr = curr.next
        return dummy.next

    def linkedList_to_arr(self, head: LinkedList) -> list[int]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

class Solution:
    def middleNode(self, head: LinkedList) -> LinkedList:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.linkedListHelper = LinkedListHelper()
        self.solution = Solution()
    
    def test_example_1(self):
        arr = [1,2,3,4,5]
        expected_output = [3,4,5]
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)

    def test_example_2(self):
        arr = [1,2,3,4,5,6]
        expected_output = [4,5,6]
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)

    def test_empty_list(self):
        arr = []
        expected_output = []
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)

    def test_single_val(self):
        arr = [1]
        expected_output = [1]
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)
    
    def test_two_val(self):
        arr = [1, 2]
        expected_output = [2]
        actual_outout = self.solution.middleNode(self.linkedListHelper.arr_to_linkedList(arr= arr))
        self.assertEqual(self.linkedListHelper.linkedList_to_arr(head= actual_outout), expected_output)

##############################
if __name__ == '__main__':
    unittest.main()




