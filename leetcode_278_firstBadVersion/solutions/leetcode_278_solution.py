class Solution:
    def __init__(self, versions: list[bool]):
        self.versions = [False] + versions  # to add version 0.
    
    def isBadVersion(self, v: int) -> bool:
        return self.versions[v]

    def firstBadVersion(self, n: int):
        left, right = 1, n
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2

            if self.isBadVersion(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans