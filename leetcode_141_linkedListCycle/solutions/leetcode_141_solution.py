from helpers.leetcode_141_helper import LinkedList

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