from heapq import heappush, heappushpop

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        find_distance = lambda x, y: x*x + y*y

        minheap = []
        for x, y in points:
            if len(minheap) < k:
                heappush(minheap, (-find_distance(x, y), x, y))
            else:
                heappushpop(minheap, (-find_distance(x, y), x, y))

        res = [[x, y] for _, x, y in minheap]
        return res

        