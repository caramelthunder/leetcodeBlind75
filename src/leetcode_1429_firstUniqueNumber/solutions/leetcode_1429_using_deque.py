from collections import deque
from typing import List


class FirstUnique:
    """
    A class to track the first unique number in a stream of numbers.

    Attributes:
        queue (deque): A queue to store the order of unique numbers.
        _is_unique (dict): Maps numbers to their uniqueness status.

    Time Complexity:
        Initialization - O(n) where n is the length of the initial nums list.
        showFirstUnique - O(k) on average, where k is the number of consecutive non-unique elements at the front of the queue.
        add - O(1)

    Space Complexity:
        O(n) where n is the number of unique numbers added.
        This is because we keep a mapping of numbers to their uniqueness and the queue itself.
    """

    def __init__(self, nums: List[int]):
        self.queue = deque([])
        self._is_unique = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        """Returns the first unique number."""
        while self.queue and not self._is_unique[self.queue[0]]:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        """Adds a number, updating the linked list and mapping accordingly."""
        if value not in self._is_unique:
            self.queue.append(value)
            self._is_unique[value] = True
        else:
            self._is_unique[value] = False
