import math
def can_eat(piles, h, val):
    t =0 
    for i in piles:
        t+=math.ceil(i/val)
        if t > h:
            return False
    return True
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start,end = 1, max(piles)
        res = 0
        while start <= end:
            mid = start + (end - start) // 2
            if can_eat(piles, h, mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res