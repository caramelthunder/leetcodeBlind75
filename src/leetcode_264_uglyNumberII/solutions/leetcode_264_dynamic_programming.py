class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0 for _ in range(n)]
        ugly_numbers[0] = 1

        i2, i3, i5 = 0, 0, 0

        for i in range(1, len(ugly_numbers)):

            num_2 = ugly_numbers[i2] * 2
            num_3 = ugly_numbers[i3] * 3
            num_5 = ugly_numbers[i5] * 5

            ugly_numbers[i] = min(num_2, num_3, num_5)

            i2 += (ugly_numbers[i] == num_2)
            i3 += (ugly_numbers[i] == num_3)
            i5 += (ugly_numbers[i] == num_5)
        
        return ugly_numbers[-1]