import math
from collections import deque

class Solution:
    def numSquares(self, n: int):
        q = deque([(n, 0)])

        while q:
            num, cnt = q.popleft()
            
            if num == 0:
                return cnt

            sqrt_num = math.sqrt(num)
            for i in range(int(sqrt_num), 0, -1):
                perfect_square = i * i

                if num - perfect_square == 0:
                    return cnt + 1
                else:
                    q.append((num - perfect_square, cnt + 1))
        
        return 1