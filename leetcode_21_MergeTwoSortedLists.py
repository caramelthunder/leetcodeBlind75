'''
Leetcode 21 - https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Helper:
    def arr_to_list(self, arr: list[int]) -> ListNode:
        if not arr:
            return None 
        dummy = ListNode()
        curr = dummy
        for val in arr:
            node = ListNode(val)
            curr.next = node
            curr = curr.next
        return dummy.next
    
    def list_to_arr(self, head: ListNode) -> list[int]:
        if not head:
            return []
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

class Solution1:
    def main(self, list1: ListNode, list2: ListNode) -> ListNode:
        node1, node2 = list1, list2
        dummy = ListNode()
        curr = dummy
        
        while node1 and node2:
            if node1.val <= node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            curr = curr.next
            
        curr.next = node1 or node2
        return dummy.next

class Solution2:
    def main(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.main(list1.next, list2)
            return list1
        else:
            list2.next = self.main(list1, list2.next)
            return list2
            
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.s1 = Solution1()
        self.s2 = Solution2()
        
    def test_both_lists_not_empty(self):
        list1 = [1,2,4]
        list2 = [1,3,4]
        expected_output = [1,1,2,3,4,4]

        solution1_ouput = self.helper.list_to_arr(self.s1.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
        solution2_ouput = self.helper.list_to_arr(self.s2.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))

        self.assertEqual(solution1_ouput, expected_output)
        self.assertEqual(solution2_ouput, expected_output)
    
    def test_one_list_empty(self):
        list1 = []
        list2 = [1,3,4]
        expected_output = [1,3,4]

        solution1_ouput = self.helper.list_to_arr(self.s1.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
        solution2_ouput = self.helper.list_to_arr(self.s2.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
            
        self.assertEqual(solution1_ouput, expected_output)
        self.assertEqual(solution2_ouput, expected_output)

    def test_both_lists_empty(self):
        list1 = []
        list2 = []
        expected_output = []

        solution1_ouput = self.helper.list_to_arr(self.s1.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
        solution2_ouput = self.helper.list_to_arr(self.s2.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
            
        self.assertEqual(solution1_ouput, expected_output)
        self.assertEqual(solution2_ouput, expected_output)
    
    def test_one_list_single_element(self):
        list1 = [5]
        list2 = []
        expected_output = [5]

        solution1_ouput = self.helper.list_to_arr(self.s1.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
        solution2_ouput = self.helper.list_to_arr(self.s2.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
            
        self.assertEqual(solution1_ouput, expected_output)
        self.assertEqual(solution2_ouput, expected_output)
    
##############################################
if __name__ == '__main__':
    unittest.main()
