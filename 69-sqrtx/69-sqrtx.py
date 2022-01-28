class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        start = 1
        end = (x//2) + 1
        while start <= end:
            mid = start + (end-start) // 2
            sqrt = mid*mid
            if sqrt <= x:
                res = mid
                start = mid + 1
            else:
                end = mid - 1
        return res