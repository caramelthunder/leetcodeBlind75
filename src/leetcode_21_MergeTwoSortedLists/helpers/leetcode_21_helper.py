class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListHelper:
    def arr_to_list(self, arr: list[int]) -> ListNode:
        if not arr:
            return None 
        dummy = ListNode()
        curr = dummy
        for val in arr:
            node = ListNode(val)
            curr.next = node
            curr = curr.next
        return dummy.next
    
    def list_to_arr(self, head: ListNode) -> list[int]:
        if not head:
            return []
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr