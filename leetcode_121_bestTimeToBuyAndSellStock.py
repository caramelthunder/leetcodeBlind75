'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

class Solution:
    def main(self, prices: list[int]) -> int:
        cheapest = float("inf")
        max_profit = 0

        for today_price in prices:
            cheapest = min(cheapest, today_price)
            max_profit = max(max_profit, today_price - cheapest)

        return max_profit

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        input_prices = [7,1,5,3,6,4]
        expected_output = 5

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)

    def test_example2(self):
        input_prices = [7,6,4,3,1]
        expected_output = 0

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)
        
    def test_increasing_prices(self):
        input_prices = [1,2,3,4,5,6,7]
        expected_output = 6

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)
        
    def test_decreasing_prices(self):
        input_prices = [7,6,5,4,3,2,1]
        expected_output = 0

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)
        
    def test_single_day(self):
        input_prices = [7]
        expected_output = 0

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)

##################################
if __name__ == '__main__':
    unittest.main()