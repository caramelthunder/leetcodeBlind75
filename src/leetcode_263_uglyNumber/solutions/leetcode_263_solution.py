class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 2:
            return n > 0

        for prime_factor in [2, 3, 5]:
            while n % prime_factor == 0:
                n = n // prime_factor
            
            if n == 1:
                return True

        return False