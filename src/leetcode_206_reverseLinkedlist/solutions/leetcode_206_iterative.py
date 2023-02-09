from helpers.leetcode_206_helper import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        tail = None

        while curr:
            next_node = curr.next
            curr.next = tail
            tail = curr
            curr = next_node
        return tail