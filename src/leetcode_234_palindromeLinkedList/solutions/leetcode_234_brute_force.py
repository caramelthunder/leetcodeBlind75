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
        The while loop for converting the linked list to a list runs in O(n) time, where n is the number of nodes in the linked list.
        The while loop for comparing the values of the nodes using two pointers runs in O(n/2) time in the worst case, where n is the length of the list.
        Therefore, the overall time complexity of the function is O(n).

        Space complexity:
        The function uses a list to store the values of the nodes in the linked list, which requires O(n) extra space, where n is the number of nodes in the linked list.
        The function uses constant extra space for the two pointers and the is_palindrome variable.
        Therefore, the overall space complexity of the function is O(n).
        """
        if head is None:
            return True

        # Convert linked-list to list.
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        # Using Two-Pointers, check if the left_val == right_val.
        is_palindrome = True

        left, right = 0, len(lst) - 1
        while left <= right:
            if lst[left] != lst[right]:
                is_palindrome = False
                break

            left += 1
            right -= 1

        return is_palindrome
