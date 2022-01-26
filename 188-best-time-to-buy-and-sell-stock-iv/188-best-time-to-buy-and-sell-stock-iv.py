class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def _max_profit(idx, is_buy, trans):
            if trans == 0 or idx == len(prices):
                return 0

            if is_buy:
                p = _max_profit(idx+1, False, trans) - prices[idx]
                skip = _max_profit(idx+1, True, trans)
            else:
                p = _max_profit(idx+1, True, trans-1) + prices[idx]
                skip = _max_profit(idx+1, False, trans)

            return max(skip, p)
        return _max_profit(0,True, k)