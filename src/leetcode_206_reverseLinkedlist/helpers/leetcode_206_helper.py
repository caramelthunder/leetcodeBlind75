class ListNode:
    def __init__(self, val= None):
        self.val = val
        self.next = None

class LinkedList_Helper:
    def list_to_linkedList(self, lst: list[int]) -> ListNode:
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def linkedList_to_list(self, head: ListNode) -> list[int]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst