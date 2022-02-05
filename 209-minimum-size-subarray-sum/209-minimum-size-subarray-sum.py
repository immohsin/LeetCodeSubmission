import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = sys.maxsize
        i = 0
        s = 0
        for j in range(len(nums)):
            s+=nums[j]
            while s >= target:
                res = min(res, j-i+1)
                s-=nums[i]
                i+=1
        return 0 if res == sys.maxsize else res
            