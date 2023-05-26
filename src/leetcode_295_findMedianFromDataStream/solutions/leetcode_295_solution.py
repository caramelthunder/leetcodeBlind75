from heapq import heappop, heappush

class MedianFinder:
    def __init__(self):
        """
        Initialize the MedianFinder object with two heaps: 
        - 'left' is a max heap for the smaller half of the numbers.
        - 'right' is a min heap for the larger half of the numbers.
        - 'even_len' is a boolean flag indicating if the total number of elements is even.
        """
        self.left = []
        self.right = []
        self.even_len = True

    def addNum(self, num: int) -> None:
        """
        Add a number into the data structure.

        Args:
            num (int): The number to be added.

        Time complexity: O(log n), where n is the number of elements added.
        Space complexity: O(1), not considering the space needed to store the elements.
        """
        if not(self.left and self.right) or self.right[0] > num:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)
        self._balance()
    
    def findMedian(self) -> float:
        """
        Find the median of all elements.

        Returns:
            float: The median of all elements. If the number of elements is even, 
            it returns the average of the two middle elements.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.even_len:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]

    def _balance(self):
        """
        Balance the two heaps to ensure the length of 'left' is always greater than or equal to the length of 'right'.

        Time complexity: O(log n), where n is the number of elements added.
        Space complexity: O(1)
        """
        while len(self.left) < len(self.right):
            heappush(self.left, -heappop(self.right))
        while len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))
        self.even_len = (len(self.left) == len(self.right))
