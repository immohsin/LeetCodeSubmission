class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def get_max_profit(idx, isBuy):
            if idx >= len(prices):
                return 0
            if isBuy:
                buy = get_max_profit(idx+1, False) - prices[idx]
                skip = get_max_profit(idx+1, True)
                profit = max(buy, skip)
            else:
                sell = get_max_profit(idx+2, True) + prices[idx]
                skip = get_max_profit(idx+1, False)
                profit = max(sell, skip)
            return profit
        return get_max_profit(0, True)