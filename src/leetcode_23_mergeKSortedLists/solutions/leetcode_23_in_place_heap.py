from typing import List, Optional
from helpers.leetcode_23_helper import ListNode
from heapq import heapify, heappush, heappop


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        """
        Merge K sorted linked lists and return the merged list.

        This function uses a priority queue (heap) to keep track of the smallest node
        among the K lists' current nodes. It continuously pops the smallest node from the
        heap, appends it to the result list, and pushes the next node from the respective list
        into the heap. This ensures that the merged list is also sorted.

        Args:
            lists (List[Optional[ListNode]]): A list containing the head nodes of
            each of the K sorted linked lists.

        Returns:
            Optional[ListNode]: The head node of the merged sorted list. Returns
            `None` if all input lists are empty.

        Runtime and space complexity:
            Time(n): O(N log K), where N is the total number of nodes in all linked lists
                     and K is the number of linked lists. The comparison cost in the heap
                     will be O(log K) and each node is entered once in the heap.

            Space(n): O(K) for the heap, as at any time, the heap will contain
                      at most K nodes (one from each list).
        """
        if not lists:
            return None

        # Populate the heap with the first node of each list
        min_heap = [
            (node.val, i, node) for i, node in enumerate(lists) if node
        ]
        heapify(min_heap)

        dummy = ListNode()
        curr = dummy

        while min_heap:
            val, i, node = heappop(min_heap)

            # Skip nodes with the same value
            while node and node.val == val:
                curr.next = node
                curr = curr.next
                node = node.next

            if node:
                heappush(min_heap, (node.val, i, node))

        return dummy.next
