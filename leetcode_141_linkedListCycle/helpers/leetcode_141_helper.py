class LinkedList:
    def __init__(self, val= None, next= None):
        self.val = val
        self.next = next
    
class LinkedListHelper: 
    def arr_to_list(self, arr: list[int], cycle_pos= -1) -> LinkedList:
        nodes_map = {}

        dummy = LinkedList()
        node = dummy

        for i in range(len(arr)):
            val = arr[i]
            new_node = LinkedList(val)
            nodes_map[i] = new_node

            node.next = new_node
            node = node.next
        
        if cycle_pos in nodes_map:
            node.next = nodes_map[cycle_pos]
        
        return dummy.next