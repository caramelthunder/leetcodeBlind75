from typing import List, Optional
from helpers.leetcode_23_helper import ListNode


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        """Merges k sorted linked lists and returns one sorted linked list.

        This function recursively divides the input lists into two halves,
        merges each half, and then merges the results of the two halves together.
        It employs a divide-and-conquer strategy similar to merge-sort.

        Args:
            lists (List[Optional[ListNode]]): A list containing the head nodes
            of k sorted linked lists. The list can be of length 0 <= k.

        Returns:
            Optional[ListNode]: The head node of the merged linked list, or `None`
            if all the input lists are empty.

        Runtime and space complexity:
            Time(n): O(Nlogk), where 'N' is the total number of nodes in all linked lists,
            and 'k' is the number of linked lists. This is because we traverse all 'N' nodes
            and divide our problem into 'k' parts in each level of recursion.

            Space(n): O(logk) due to the recursive stack if the function is implemented recursively.
            The overall space complexity (considering the new linked list) can be O(N).
        """

        def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1 or not l2:
                return l1 or l2

            if l1.val < l2.val:
                l1.next = merge_two_lists(l1.next, l2)
                return l1
            else:
                l2.next = merge_two_lists(l1, l2.next)
                return l2

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return merge_two_lists(lists[0], lists[1])

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge_two_lists(left, right)
