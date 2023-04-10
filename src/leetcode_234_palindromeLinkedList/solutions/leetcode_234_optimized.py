from helpers.leetcode_234_helper import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Checks whether a linked list is a palindrome.

        Args:
            head: The head of the linked list.
        Returns:
            True if the linked list is a palindrome, False otherwise.
        
        Time complexity:
        O(n) - The function loops through the linked list twice using the two pointers technique, 
        and reverses a portion of the list.
        
        Space complexity:
        O(1) - The function only uses a constant amount of extra space for the two pointers 
        and the temporary variables used during the reversal of the linked list.
        """
        if head is None:
            return True
        
        # Find the middle of the linked list using the two pointers technique
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the right half of the linked list
        right_half = slow if fast is None else slow.next
        rev_right_half = self.reverse_linkedList(right_half)

        # Compare the left and right halves of the linked list
        is_palindrome = True
        
        left_head, right_head = head, rev_right_half
        while left_head is not None and right_head is not None:
            if left_head.val != right_head.val:
                is_palindrome = False
                break
            
            left_head = left_head.next
            right_head = right_head.next

        # Reverse the right half of the linked list again to restore the original linked list
        self.reverse_linkedList(rev_right_half)

        return is_palindrome
    
    def reverse_linkedList(self, head):
        """
        Reverses a linked list and returns the new head.
        """
        curr = head
        tail = None

        while curr is not None:
            _next = curr.next
            curr.next = tail
            tail = curr
            curr = _next
            
        return tail
