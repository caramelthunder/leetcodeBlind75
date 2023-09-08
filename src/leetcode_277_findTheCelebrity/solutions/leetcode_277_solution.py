class Knows:
    def __init__(self, matrix: list[list[int, int]]):
        self.matrix = matrix

    def knows(self, a: int, b: int) -> bool:
        return self.matrix[a][b] == 1


class Solution(Knows):
    def __init__(self, matrix: list[list[int, int]]):
        super().__init__(matrix)

    def findCelebrity(self, n: int) -> int:
        """
        Find the celebrity in a group of n individuals. A celebrity is defined as
        an individual who is known by everyone else but does not know anyone else.

        :param n: Integer representing the number of individuals.

        :return: Integer representing the celebrity, or -1 if there is no celebrity.

        Time Complexity: O(n), where n is the number of individuals.
        Space Complexity: O(n), due to the cache dictionary storing at most n entries.
        """
        if n < 2:
            return n - 1

        candidate = 0

        for person in range(1, n):
            if self.knows(candidate, person):
                candidate = person

        for person in range(n):
            if person != candidate:
                if self.knows(candidate, person) or not self.knows(
                    person, candidate
                ):
                    return -1

        return candidate
