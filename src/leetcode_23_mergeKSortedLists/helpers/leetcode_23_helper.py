# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeHelper:
    def arr_to_linked_list(self, arr: list[int]) -> ListNode:
        if not arr:
            return None
        node = ListNode(arr[0])
        node.next = self.arr_to_linked_list(arr[1:])
        return node

    def linked_list_to_arr(self, head: ListNode) -> list[int]:
        if not head:
            return []
        return [head.val] + self.linked_list_to_arr(head.next)
