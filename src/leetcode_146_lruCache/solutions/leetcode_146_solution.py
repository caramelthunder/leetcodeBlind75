class DoubleLinkedNode:
    def __init__(self, key= None, val= None):
        self.prev = None
        self.key = key
        self.val = val
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self._link_nodes(self.head, self.tail)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.capacity == 0:
                self._cache_evict()

            new_node = DoubleLinkedNode(key= key, val= value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            self.capacity -= 1
        else:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        
    def _cache_evict(self):
        tobe_evicted = self.tail.prev
        self._link_nodes(tobe_evicted.prev, tobe_evicted.next)

        tobe_evicted.prev, tobe_evicted.next = None, None
        del self.cache[tobe_evicted.key]
        self.capacity += 1

    def _move_to_front(self, node: DoubleLinkedNode):
        self._link_nodes(node.prev, node.next)
        self._add_to_front(node)
    
    def _add_to_front(self, node: DoubleLinkedNode):
        self._link_nodes(node, self.head.next)
        self._link_nodes(self.head, node)

    def _link_nodes(self, a: DoubleLinkedNode, b: DoubleLinkedNode):
        a.next = b
        b.prev = a