
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        find_distance = lambda x, y: x*x + y*y

        points.sort(key= lambda point: find_distance(*point))
        res = [points[i] for i in range(k)]
        return res

        