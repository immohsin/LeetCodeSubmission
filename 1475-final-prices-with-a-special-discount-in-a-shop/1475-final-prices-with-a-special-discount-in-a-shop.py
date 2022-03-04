class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        res = [0] * len(prices)
        for p in range(len(prices)):
            while s and prices[s[-1]] >= prices[p]:
                idx = s.pop()
                res[idx] = prices[idx] - prices[p]
            s.append(p)
        while s:
            idx = s.pop()
            res[idx] = prices[idx]
        return res
            
            
