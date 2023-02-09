class Solution:
    def main(self, prices: list[int]) -> int:
        cheapest = float("inf")
        max_profit = 0

        for today_price in prices:
            cheapest = min(cheapest, today_price)
            max_profit = max(max_profit, today_price - cheapest)

        return max_profit