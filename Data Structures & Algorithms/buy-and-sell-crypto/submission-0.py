class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price          # found a new best "buy" day
            else:
                profit = max(profit, price - min_price)  # try selling today

        return profit