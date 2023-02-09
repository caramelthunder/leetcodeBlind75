class Solution:
    def climbStairs(self, n: int) -> int:
        from_one = 1
        from_two = 1

        for _ in range(2, n + 1):
            curr = from_one + from_two
            from_two = from_one
            from_one = curr

        return curr