from typing import Optional

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the n-th node from the end of the linked list.

        Args:
            head (Optional[ListNode]): The head of the input linked list.
            n (int): The position of the node to remove, counted from the end of the list.

        Returns:
            Optional[ListNode]: The head of the modified linked list after removing the n-th node from the end.

        Time Complexity Analysis:
            O(2L): Where L is the number of nodes in the linked list. 
                   We traverse the list twice - once to find the length of the list, 
                   and a second time to locate and remove the n-th node from the end.
                   The time complexity is linear in terms of the number of nodes in the list.

        Space Complexity Analysis:
            O(1): We only use a constant amount of extra space for the dummy ListNode and a few pointers.
        """
        _len = 0
        curr = head
        while curr is not None:
            _len += 1
            curr = curr.next

        dummy = ListNode()
        dummy.next = head
        curr = dummy
        for _ in range(_len - n):
            curr = curr.next

        tobe_removed = curr.next
        curr.next = tobe_removed.next
        tobe_removed.next = None

        return dummy.next
