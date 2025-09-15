class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        buy = prices[0]
        profit = 0
        while r < len(prices):
            profit = max(prices[r] - buy, profit)
            if prices[r] <= buy:
                l = r
                buy = prices[r]
            r += 1
        return profit
