import sys
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        t = []
        i = 0
        mmax, mmin = nums[0], nums[0]
        res = sys.maxsize
        for j in range(0, len(nums)):
            t.append(nums[j])
            if j-i+1 == k:
                res = min(res, max(t) - min(t))
                if t[0] == nums[i]:
                    t.pop(0)
                i+=1
        return res