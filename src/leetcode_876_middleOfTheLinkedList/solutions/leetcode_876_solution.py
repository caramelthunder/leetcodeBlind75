from helpers.leetcode_876_helper import LinkedList

class Solution:
    def middleNode(self, head: LinkedList) -> LinkedList:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        