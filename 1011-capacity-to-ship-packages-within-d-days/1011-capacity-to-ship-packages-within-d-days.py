def isPossible(weights, days, mid):
    a_day = 1
    s = 0
    for i in range(len(weights)):
        if weights[i] > mid:
            return False
        s+=weights[i]
        if s > mid:
            a_day+= 1
            s = weights[i]
        if a_day > days:
            return False
    return True
        
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) < days:
            return -1
        
        start, end = max(weights), sum(weights)
        res = 0
        while start <= end:
            mid = start + (end - start) // 2
            if isPossible(weights, days, mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return start   