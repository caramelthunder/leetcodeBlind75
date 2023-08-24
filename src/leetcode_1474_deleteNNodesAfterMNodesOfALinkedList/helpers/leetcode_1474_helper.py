class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListHelper:
    def arr_to_list(self, arr: list[int], head_pos=0) -> ListNode:
        if not arr or head_pos >= len(arr):
            return None
        head = ListNode(arr[head_pos])
        head.next = self.arr_to_list(arr, head_pos + 1)
        return head

    def list_to_arr(self, head: ListNode) -> list[int]:
        if not head:
            return []
        return [head.val] + self.list_to_arr(head.next)
