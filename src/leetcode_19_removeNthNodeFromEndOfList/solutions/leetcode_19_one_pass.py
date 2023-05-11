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
            Optional[ListNode]: The head of the modified linked list
                                after removing the n-th node from the end.

        Time Complexity Analysis:
            O(L): Where L is the number of nodes in the linked list.
                  We traverse the list once with two pointers (slow, fast),
                  maintaining a gap of n nodes between them. The time complexity is therefore linear.

        Space Complexity Analysis:
            O(1): We only use a constant amount of extra space for
                  the dummy ListNode and the two pointers (slow, fast).
        """
        dummy = ListNode(next=head)

        slow, fast = dummy, dummy
        while fast is not None and n > 0:
            fast = fast.next
            n -= 1

        if fast is None:
            return None

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        tobe_removed = slow.next
        slow.next = tobe_removed.next
        tobe_removed.next = None

        return dummy.next
