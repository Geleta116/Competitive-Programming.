class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx, i in enumerate(prices[1:]):
            profit += max(0, i - prices[idx])
        return profit