import sys
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        t = []
        i = 0
        res = sys.maxsize
        for j in range(0, len(nums)):
            if j-i+1 == k:
                res = min(res, nums[j]-nums[i])
                i+=1
        return res