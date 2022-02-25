class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 0, n
        res = 0
        while start <= end:
            mid = start + (end - start) // 2
            k = (mid * (mid+1)) // 2
            if k == n:
                res = mid
                break
            elif k > n:
                end = mid - 1
            else:
                res = mid
                start = mid + 1
        return res
                
            
                