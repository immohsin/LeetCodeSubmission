class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        i = 1
        while i <= (x//2)+1:
            if i*i <= x:
                res = i
            else:
                break
            i+=1
        return res