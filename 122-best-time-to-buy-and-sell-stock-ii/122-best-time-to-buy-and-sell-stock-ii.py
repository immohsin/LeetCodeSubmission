class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pur = prices[0]
        res = 0
        for i in range(1, len(prices)):
            profit = prices[i] - pur
            if profit > 0:
                res+=profit
            pur = prices[i]
        return res