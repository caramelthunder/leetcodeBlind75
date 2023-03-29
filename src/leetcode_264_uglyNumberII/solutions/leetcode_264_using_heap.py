from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num = 1
        seen = set()
        min_heap = [1]

        while n > 0:
            ugly_num = heappop(min_heap)
            n -= 1

            for prime_factor in [2, 3, 5]:
                if ugly_num * prime_factor not in seen:
                    seen.add(ugly_num * prime_factor)
                    heappush(min_heap, ugly_num * prime_factor)

        return ugly_num