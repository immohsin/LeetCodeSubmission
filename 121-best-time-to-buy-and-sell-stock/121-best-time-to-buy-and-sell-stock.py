class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        pur = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - pur
            if profit < 0:
                pur = prices[i]
            res = max(profit, res)
        return res