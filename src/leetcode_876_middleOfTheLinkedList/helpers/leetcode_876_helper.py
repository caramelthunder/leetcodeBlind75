class LinkedList:
    def __init__(self, val= None):
        self.val = val
        self.next = None

class LinkedListHelper:
    def arr_to_linkedList(self, arr: list[int]) -> LinkedList:
        dummy = LinkedList()
        curr = dummy
        for val in arr:
            curr.next = (LinkedList(val))
            curr = curr.next
        return dummy.next

    def linkedList_to_arr(self, head: LinkedList) -> list[int]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr