import sys

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        res = -sys.maxsize
        s = 0
        for j in range(len(nums)):
            s+=nums[j]
            if j-i+1 == k:
                res = max(res, (s/k))
                s-=nums[i]
                i+=1
        return res
            