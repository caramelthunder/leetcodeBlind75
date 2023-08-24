from helpers.leetcode_1474_helper import ListNode


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        Given a linked list and two integers m and n, traverse the linked list
        and remove every n nodes after keeping m nodes.

        Args:
        - head (ListNode): The head of the linked list.
        - m (int): The number of nodes to keep.
        - n (int): The number of nodes to remove.

        Returns:
        - ListNode: The head of the modified linked list.

        Time Complexity:
        - O(m + n) for each iteration through the linked list.

        Space Complexity:
        - O(1), since we are modifying the input linked list in-place.
        """
        # initial dummy node for easier handling of head
        dummy = ListNode(None, head)
        current_node, next_node = dummy, dummy

        while current_node:
            _m, _n = 0, 0

            # Traverse the m nodes to keep
            while current_node and _m < m:
                current_node = current_node.next
                next_node = current_node
                _m += 1

            # Traverse the n nodes to delete
            while next_node and _n <= n:
                next_node = next_node.next
                _n += 1

            # Connect the mth node to the node after nth node
            if current_node:
                current_node.next = next_node

        return dummy.next
