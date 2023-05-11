from typing import List, Optional

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedListHelper:
    def arr_to_list(self, arr: List[int]) -> ListNode:
        dummy = ListNode()
        curr = dummy
        for num in arr:
            curr.next = ListNode(val=num)
            curr = curr.next
        return dummy.next

    def list_to_arr(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        curr = head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        return arr