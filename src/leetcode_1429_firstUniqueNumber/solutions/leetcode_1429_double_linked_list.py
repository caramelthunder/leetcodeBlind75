from typing import List


class _DoubleLinkedListNode:
    """Node for the doubly linked list."""

    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class FirstUnique:
    """
    A class to track the first unique number in a stream of numbers.

    Attributes:
        num_map (dict): Maps numbers to their corresponding linked list nodes.
        head (DoubleLinkedListNode): Dummy head node of the linked list.
        tail (DoubleLinkedListNode): Dummy tail node of the linked list.

    Time Complexity:
        Initialization - O(n) where n is the length of the initial nums list.
        showFirstUnique - O(1)
        add - O(1)

    Space Complexity:
        O(n) where n is the number of unique numbers added.
        This is because we keep a mapping of numbers to their linked list nodes and the linked list itself.
    """

    def __init__(self, nums: List[int]):
        self.num_map = {}
        self.head = _DoubleLinkedListNode(-1)
        self.tail = _DoubleLinkedListNode(-1)
        self._link_nodes(self.head, self.tail)

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        """Returns the first unique number."""
        return self.head.next.val

    def add(self, value: int) -> None:
        """Adds a number, updating the linked list and mapping accordingly."""
        if value not in self.num_map:
            _unique = _DoubleLinkedListNode(value)
            self.num_map[value] = _unique
            self._append_node(_unique)
        else:
            _not_unique = self.num_map[value]
            self.num_map[value] = None
            self._remove_node(_not_unique)

    def _remove_node(self, node) -> None:
        """Removes a given node from the linked list."""
        if node:
            self._link_nodes(node.prev, node.next)
            node.prev, node.next = None, None

    def _append_node(self, node) -> None:
        """Appends a given node to the end of the unique linked list."""
        self._link_nodes(self.tail.prev, node)
        self._link_nodes(node, self.tail)

    def _link_nodes(
        self, a: _DoubleLinkedListNode, b: _DoubleLinkedListNode
    ) -> None:
        """Links two nodes together."""
        a.next = b
        b.prev = a
