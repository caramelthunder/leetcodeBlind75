from helpers.leetcode_206_helper import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self._reverseList(head, None)

    def _reverseList(self,curr, tail):
        if not curr:
            return tail
        next_node = curr.next
        curr.next = tail
        return self._reverseList(next_node, curr)