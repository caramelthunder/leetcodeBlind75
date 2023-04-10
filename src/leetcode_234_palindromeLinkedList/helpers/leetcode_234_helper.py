class ListNode:
    def __init__(self, val= 0):
        self.val = val
        self.next = None

class LinkedList_Helper:    
    def lst_to_linkedLst(self, lst: list[int]) -> ListNode:
        if not lst:
            return None
            
        dummy = ListNode()
        curr = dummy
        
        for num in lst:
            node = ListNode(val= num)
            curr.next = node
            curr = curr.next
            
        return dummy.next
