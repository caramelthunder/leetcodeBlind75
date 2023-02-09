from helpers.leetcode_21_helper import ListNode

class Solution:
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